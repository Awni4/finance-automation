"""
Finance Automation – Kontoauszug einlesen und auswerten

Funktionsumfang:
1. Liest einen Kontoauszug im deutschen CSV-Format ein (Semikolon, Komma als Dezimaltrennzeichen)
2. Wandelt Datum und Beträge in echte Datentypen um
3. Ordnet jede Buchung automatisch einer Kategorie zu
4. Gibt Auswertungen aus: Monatsübersicht, größte Ausgaben, Ausgaben nach Kategorie und nach Kategorie und Monat

Ausführen (im Projektordner):
    python src/main.py
"""

from pathlib import Path

import pandas as pd

from kategorien import kategorisieren

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
    return df


def monatsuebersicht(df: pd.DataFrame) -> pd.DataFrame:
    """Berechnet Einnahmen, Ausgaben und Saldo pro Monat."""
    df = df.copy()
    df["monat"] = df["datum"].dt.to_period("M")
    uebersicht = df.groupby("monat").agg(
        einnahmen=("betrag", lambda b: b[b > 0].sum()),
        ausgaben=("betrag", lambda b: b[b < 0].sum()),
        saldo=("betrag", "sum"),
        buchungen=("betrag", "count"),
    )
    return uebersicht.round(2)


def kategorien_pro_monat(df: pd.DataFrame) -> pd.DataFrame:
    """Summiert die Beträge pro Kategorie und Monat."""
    df = df.copy()
    df["monat"] = df["datum"].dt.to_period("M")
    tabelle = pd.pivot_table(
        df,
        index="kategorie",
        columns="monat",
        values="betrag",
        aggfunc="sum",
        fill_value=0,
    )
    return tabelle.round(2)


def main() -> None:
    df = kontoauszug_laden(DATEI)
    df["kategorie"] = df["text"].apply(kategorisieren)

    print(f"{len(df)} Buchungen eingelesen "
          f"({df['datum'].min():%d.%m.%Y} bis {df['datum'].max():%d.%m.%Y})\n")

    print("=== Monatsübersicht ===")
    print(monatsuebersicht(df).to_string())

    print("\n=== Die 5 größten Ausgaben ===")
    top = df.nsmallest(5, "betrag")[["datum", "text", "betrag"]]
    print(top.to_string(index=False))

    print("\n=== Ausgaben nach Kategorie ===")
    print(df.groupby("kategorie")["betrag"].sum().round(2).sort_values().to_string())

    print("\n=== Ausgaben nach Kategorie und Monat ===")
    print(kategorien_pro_monat(df).to_string())


if __name__ == "__main__":
    main()
