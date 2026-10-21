"""Ordnet Buchungen anhand von Suchbegriffen einer Kategorie zu."""

KATEGORIEN = {
    "Einkommen": ["Gehalt"],
    "Lebensmittel": ["REWE", "ALDI", "LIDL"],
    "Wohnen": ["Miete"],
    "Gesundheit": ["Apotheke"],
    "Mobilität": ["Shell", "Deutsche Bahn"],
    "Abos & Verträge": ["Spotify", "Netflix", "FitX"],
    "Mobilfunk": ["Vodafone"],
    "Online Shopping": ["Amazon"],
    "Essen außerhalb": ["Lieferando", "Restaurant"],
    "Pflege": ["dm-drogerie"],
}


def kategorisieren(text: str) -> str:
    """Gibt die passende Kategorie für einen Buchungstext zurück."""
    text = text.upper()
    for kategorie, suchbegriffe in KATEGORIEN.items():
        for begriff in suchbegriffe:
            if begriff.upper() in text:
                return kategorie
    return "Sonstiges"