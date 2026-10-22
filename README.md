# Finance Automation

Automatisierte Auswertung von Kontoauszügen mit Python: Buchungen einlesen, automatisch kategorisieren, Auffälligkeiten erkennen und einen Monatsbericht erzeugen.

>**Status:** in Entwicklung – Fortschritt wird regelmäßig im [Entwicklungstagebuch](DEVLOG.md) dokumentiert.

## Problem

Viele Finanzprozesse laufen noch manuell: Kontoauszüge werden in Excel kopiert, Buchungen von Hand kategorisiert, Auffälligkeiten (Doppelbuchungen, ungewöhnlich hohe Beträge) fallen erst spät auf. Das kostet Zeit und ist fehleranfällig.

## Lösung

Dieses Projekt automatisiert den Ablauf von der CSV-Datei bis zum fertigen Bericht:

1. **Einlesen** – deutsches Bank-CSV-Format (Semikolon, Dezimalkomma)
2. **Kategorisieren** – regelbasiert (z. B. „REWE“ → Lebensmittel), später mit KI
3. **Prüfen** – Doppelbuchungen und ungewöhnlich hohe Ausgaben markieren
4. **Berichten** – Monatsübersicht mit Diagrammen als Excel/HTML

## Funktionen

- [x] Kontoauszug einlesen und bereinigen
- [x] Monatsübersicht (Einnahmen, Ausgaben, Saldo)
- [x] Automatische Kategorisierung
- [x] Auswertung nach Kategorie und Monat (Pivot-Tabelle)
- [ ] Erkennung von Auffälligkeiten
- [ ] Diagramme
- [ ] Export als Excel-Bericht
- [ ] Prozessmodell (BPMN) Vorher/Nachher

## Technologien

Python · pandas · (geplant: matplotlib, openpyxl, BPMN)

## Installation & Nutzung

```bash
git clone https://github.com/Awni4/finance-automation.git
cd finance-automation
pip install -r requirements.txt
python src/main.py
```

## Daten

Alle Daten im Ordner `data/` sind **frei erfunden**. Es werden keine echten Bank- oder Personendaten verwendet.

## Autor

Awni Badlah – Student der Wirtschaftsinformatik, Schwerpunkt KI, Finanzen und Prozessautomatisierung

Entwickelt mit KI-Unterstützung (Claude) als Lern- und Portfolioprojekt.
