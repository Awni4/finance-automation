"""Exportiert die Auswertungen als Excel-Bericht."""

from datetime import datetime
from pathlib import Path

import pandas as pd

AUSGABE_ORDNER = Path(__file__).parent.parent / "output"


def excel_bericht_erstellen(blaetter: dict[str, pd.DataFrame]) -> Path:
    """Schreibt jede Tabelle in ein eigenes Tabellenblatt und gibt den Dateipfad zurück."""
    AUSGABE_ORDNER.mkdir(exist_ok=True)
    pfad = AUSGABE_ORDNER / "finanzbericht.xlsx"
    with pd.ExcelWriter(pfad, engine="openpyxl") as writer:
        for name, tabelle in blaetter.items():
            tabelle.to_excel(writer, sheet_name=name, index=False)
            blatt_formatieren(writer.sheets[name])
    return pfad


def blatt_formatieren(blatt) -> None:
    """Formatiert Datum und Beträge im deutschen Format und passt die Spaltenbreite an."""
    for spalte in blatt.columns:
        for zelle in spalte[1:]:
            if isinstance(zelle.value, datetime):
                zelle.number_format = "DD.MM.YYYY"
            elif isinstance(zelle.value, float):
                zelle.number_format = "#,##0.00"
        breite = max(len(str(zelle.value)) for zelle in spalte if zelle.value is not None)
        blatt.column_dimensions[spalte[0].column_letter].width = min(breite + 2, 40)