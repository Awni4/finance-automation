"""
Finance Automation – Kontoauszug einlesen und auswerten

Funktionsumfang:
1. Liest einen Kontoauszug im deutschen CSV-Format ein (Semikolon, Komma als Dezimaltrennzeichen)
2. Wandelt Datum und Beträge in echte Datentypen um
3. Ordnet jede Buchung automatisch einer Kategorie zu
4. Gibt Auswertungen aus: Monatsübersicht, größte Ausgaben, Ausgaben nach Kategorie und nach Kategorie und Monat (ohne Einnahmen)
5. Erkennt Verdachtsfälle auf Doppelbuchungen (gleicher Text, Betrag und Monat)
6. Erkennt ungewöhnlich hohe Ausgaben (mehr als das Dreifache des Medians ihrer Kategorie)
7. Erstellt Diagramme (PNG) und einen Excel-Bericht mit allen Auswertungen im Ordner output

Ausführen (im Projektordner):
    python src/main.py
"""

from pathlib import Path

import pandas as pd

from kategorien import kategorisieren
from diagramme import diagramm_ausgaben_nach_kategorie, diagramm_saldo_pro_monat
from bericht import excel_bericht_erstellen

# Pfad zur Datei – relativ zum Projektordner, damit es auf jedem Rechner funktioniert
DATEI = Path(__file__).parent.parent / "data" / "kontoauszug_beispiel.csv"


def kontoauszug_laden(pfad: Path) -> pd.DataFrame:
    """Liest den Kontoauszug ein und bereinigt die Datentypen."""
    df = pd.read_csv(
        pfad,
        sep=";",          # deutsche Banken trennen Spalten meist mit Semikolon
        decimal=",",      # und schreiben 12,50 statt 12.50
        encoding="utf-8",
    )
    # Spalten umbenennen: kurze Namen ohne Leerzeichen sind im Code angenehmer
    df = df.rename(columns={
        "Buchungstag": "datum",
        "Verwendungszweck": "text",
        "Betrag (EUR)": "betrag",
    })
    # Text "01.07.2026" in ein echtes Datum umwandeln
    df["datum"] = pd.to_datetime(df["datum"], format="%d.%m.%Y")
    # Monat als eigene Spalte, wird von mehreren Auswertungen genutzt
    df["monat"] = df["datum"].dt.to_period("M")
    return df


def nur_ausgaben(df: pd.DataFrame) -> pd.DataFrame:
    """Gibt nur die Ausgaben (negative Beträge) zurück."""
    return df[df["betrag"] < 0]


def monatsuebersicht(df: pd.DataFrame) -> pd.DataFrame:
    """Berechnet Einnahmen, Ausgaben und Saldo pro Monat."""
    uebersicht = df.groupby("monat").agg(
        einnahmen=("betrag", lambda b: b[b > 0].sum()),
        ausgaben=("betrag", lambda b: b[b < 0].sum()),
        saldo=("betrag", "sum"),
        buchungen=("betrag", "count"),
    )
    return uebersicht.round(2)


def kategorien_pro_monat(df: pd.DataFrame) -> pd.DataFrame:
    """Summiert die Beträge pro Kategorie und Monat."""
    tabelle = pd.pivot_table(
        df,
        index="kategorie",
        columns="monat",
        values="betrag",
        aggfunc="sum",
        fill_value=0,
    )
    return tabelle.round(2)


def doppelbuchungen_finden(df: pd.DataFrame) -> pd.DataFrame:
    """Findet Buchungen, die im selben Monat mit gleichem Text und Betrag mehrfach vorkommen."""
    doppelt = df.duplicated(subset=["text", "monat", "betrag"], keep=False)
    return df[doppelt]


def ausreisser_finden(df: pd.DataFrame, faktor: float = 3) -> pd.DataFrame:
    """Findet Ausgaben, die mehr als das faktor-fache des Medians ihrer Kategorie betragen."""
    ausgaben = nur_ausgaben(df)
    median = ausgaben.groupby("kategorie")["betrag"].transform("median")
    auffaellig = ausgaben["betrag"] < faktor * median
    return ausgaben[auffaellig]


def main() -> None:
    df = kontoauszug_laden(DATEI)
    df["kategorie"] = df["text"].apply(kategorisieren)
    ausgaben = nur_ausgaben(df)

    print(f"{len(df)} Buchungen eingelesen "
          f"({df['datum'].min():%d.%m.%Y} bis {df['datum'].max():%d.%m.%Y})\n")

    print("=== Monatsübersicht ===")
    print(monatsuebersicht(df).to_string())

    print("\n=== Die 5 größten Ausgaben ===")
    top = df.nsmallest(5, "betrag")[["datum", "text", "betrag"]]
    print(top.to_string(index=False))

    print("\n=== Ausgaben nach Kategorie ===")
    print(ausgaben.groupby("kategorie")["betrag"].sum().round(2).sort_values().to_string())

    print("\n=== Ausgaben nach Kategorie und Monat ===")
    print(kategorien_pro_monat(ausgaben).to_string())

    print("\n=== Verdacht auf Doppelbuchungen ===")
    doppelte = doppelbuchungen_finden(df)[["datum", "text", "betrag"]]
    print(doppelte.to_string(index=False))

    print("\n=== Ungewöhnlich hohe Ausgaben ===")
    ausreisser = ausreisser_finden(df)[["datum", "text", "betrag", "kategorie"]]
    print(ausreisser.to_string(index=False))

    pfad = diagramm_ausgaben_nach_kategorie(ausgaben)
    print(f"\nDiagramm gespeichert: {pfad}")

    pfad = diagramm_saldo_pro_monat(monatsuebersicht(df))
    print(f"Diagramm gespeichert: {pfad}")

    blaetter = {
        "Buchungen": df,
        "Monatsübersicht": monatsuebersicht(df).reset_index(),
        "Ausgaben pro Monat": kategorien_pro_monat(ausgaben).reset_index(),
        "Doppelbuchungen": doppelbuchungen_finden(df),
        "Ungewöhnlich hohe Ausgaben": ausreisser_finden(df),
    }
    pfad = excel_bericht_erstellen(blaetter)
    print(f"Excel-Bericht gespeichert: {pfad}")


if __name__ == "__main__":
    main()