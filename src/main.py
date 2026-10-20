"""
Finance Automation – Tag 1: Kontoauszug einlesen und erste Übersicht

Was dieses Skript macht:
1. Liest einen Kontoauszug im deutschen CSV-Format ein (Semikolon, Komma als Dezimaltrennzeichen)
2. Wandelt Datum und Beträge in echte Datentypen um
3. Gibt eine erste Übersicht aus: Einnahmen, Ausgaben, Saldo pro Monat

Ausführen (im Projektordner):
    python src/main.py
"""

from pathlib import Path

import pandas as pd

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


def main() -> None:
    df = kontoauszug_laden(DATEI)

    print(f"{len(df)} Buchungen eingelesen "
          f"({df['datum'].min():%d.%m.%Y} bis {df['datum'].max():%d.%m.%Y})\n")

    print("=== Monatsübersicht ===")
    print(monatsuebersicht(df).to_string())

    print("\n=== Die 5 größten Ausgaben ===")
    top = df.nsmallest(5, "betrag")[["datum", "text", "betrag"]]
    print(top.to_string(index=False))


if __name__ == "__main__":
    main()
