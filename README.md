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
- [x] Erkennung von Doppelbuchungen
- [x] Erkennung ungewöhnlich hoher Ausgaben
- [x] Diagramme
- [ ] Export als Excel-Bericht
- [ ] Prozessmodell (BPMN) Vorher/Nachher

## Beispielausgabe

Auszug aus der Auswertung der Beispieldaten (Juli–September 2026):

```text
=== Ausgaben nach Kategorie und Monat ===
monat            2026-07  2026-08  2026-09
kategorie
Abos & Verträge   -49.97   -49.97   -60.96
Essen außerhalb  -140.99   -77.47  -124.24
Gesundheit         -9.62     0.00   -40.58
Lebensmittel     -189.98  -218.73  -114.98
Mobilfunk         -19.99   -19.99   -19.99
Mobilität         -46.51  -186.79  -135.52
Online Shopping  -185.91  -718.18   -21.64
Pflege              0.00   -23.25     0.00
Wohnen           -520.00  -520.00  -520.00

=== Verdacht auf Doppelbuchungen ===
     datum       text  betrag
2026-09-03 Spotify AB  -10.99
2026-09-12 Spotify AB  -10.99

=== Ungewöhnlich hohe Ausgaben ===
     datum               text  betrag       kategorie
2026-08-19 Amazon EU S.a.r.l.  -649.0 Online Shopping
```

Auf einen Blick wird sichtbar, in welchem Monat welche Kategorie vom Normalwert abweicht. Auffälligkeiten wie die doppelte Spotify-Abbuchung im September und der ungewöhnlich hohe Amazon-Einkauf über 649 € im August werden automatisch erkannt, ohne dass die Buchungen manuell durchgesehen werden müssen.

## Technologien

Technologien: Python · pandas · matplotlib · (geplant: openpyxl, BPMN)

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