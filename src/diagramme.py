"""Erstellt Diagramme zur Auswertung der Ausgaben."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

AUSGABE_ORDNER = Path(__file__).parent.parent / "output"


def diagramm_ausgaben_nach_kategorie(ausgaben: pd.DataFrame) -> Path:
    """Speichert ein Balkendiagramm der Ausgaben pro Kategorie und gibt den Dateipfad zurück."""
    summen = ausgaben.groupby("kategorie")["betrag"].sum().abs().sort_values()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(summen.index, summen.values)
    ax.set_title("Ausgaben nach Kategorie (Juli–September 2026)")
    ax.set_xlabel("Euro")
    fig.tight_layout()

    AUSGABE_ORDNER.mkdir(exist_ok=True)
    pfad = AUSGABE_ORDNER / "ausgaben_nach_kategorie.png"
    fig.savefig(pfad, dpi=150)
    plt.close(fig)
    return pfad

def diagramm_saldo_pro_monat(uebersicht: pd.DataFrame) -> Path:
    """Speichert ein Balkendiagramm des Saldos pro Monat und gibt den Dateipfad zurück."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(uebersicht.index.astype(str), uebersicht["saldo"])
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("Saldo pro Monat (Juli–September 2026)")
    ax.set_ylabel("Euro")
    fig.tight_layout()

    AUSGABE_ORDNER.mkdir(exist_ok=True)
    pfad = AUSGABE_ORDNER / "saldo_pro_monat.png"
    fig.savefig(pfad, dpi=150)
    plt.close(fig)
    return pfad