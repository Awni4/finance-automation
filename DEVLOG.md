# Entwicklungstagebuch


**Vorlage:**
```
## Tag X – TT.MM.JJJJ
**Erledigt:**
**Gelernt:**
**Problem & Lösung:**
**Nächster Schritt:**
```

---

## Tag 1 – 20.10.2026
**Erledigt:** Projektstruktur angelegt, fiktiven Kontoauszug (62 Buchungen, Juli–September 2026) erstellt, Skript zum Einlesen und für die Monatsübersicht geschrieben, Projekt auf GitHub hochgeladen.

**Gelernt:** -

**Problem & Lösung:** -

**Nächster Schritt:** Händler automatisch in Kategorien einordnen (Tag 2).

## Tag 2 – 21.10.2026
**Erledigt:**
Kategorien angesetzt, Ausgaben werden jetzt sinnvoll kategorisiert -> Übersichtlichkeit

**Gelernt:**
KI hat die ersten 2 Kategorien erstellt, ich habe die restlichen ergänzen wollen, sodass nichts mehr unter "Sonstiges" fällt und alles sinnvoll kategorisiert ist.

Python lokal installieren und Bibliotheken mit pip verwalten; Dictionaries in Python; Funktionen aus einer eigenen Datei importieren; Suchbegriffe präzise wählen (z. B. „dm-drogerie“ statt „dm“, um Fehlzuordnungen zu vermeiden).

**Problem & Lösung:**
-Problem: Zu viele Umsätze -> schwer alles zuzuordnen und ist unübersichtlich
-Lösung: Durch Kategorien schafft man es die Umsätze besser im Blick zu behalten.


-> Die Kategorisierung ermöglicht es Privatpersonen, ihre größten Ausgabenposten auf einen Blick zu erkennen und so gezielt Einsparpotenziale zu identifizieren.



Beim ersten Ausführen erschien `ModuleNotFoundError: No module named 'pandas'`. Ursache: Die Bibliothek war noch nicht installiert. Lösung: Installation mit `python -m pip install -r requirements.txt`.


**Nächster Schritt:**
Ausgaben pro Kategorie und Monat in einer Pivot-Tabelle auswerten, um monatliche Abweichungen zu erkennen.

## Tag 3 – 22.10.2026
**Erledigt:**
Pivot-Tabelle erstellt (neue Funktion `kategorien_pro_monat`), Ausgaben werden jetzt pro Kategorie und Monat dargestellt -> Entwicklung der Ausgaben über die Zeit sichtbar

Code aufgeräumt: Beschreibung am Anfang von `main.py` aktualisiert.

**Gelernt:**
Aufbau einer Pivot-Tabelle mit pandas: `index` bestimmt die Zeilen, `columns` die Spalten, `values` die berechneten Werte (vergleichbar mit Zeilen, Spalten und Werten in einer Excel-Pivot-Tabelle); Vertauschen von `index` und `columns` dreht die Tabelle nur (transponiert), die Werte bleiben gleich.

Unterschied zwischen Funktion definieren (`def`) und Funktion aufrufen; Reihenfolge im Code beachten (die Spalte „kategorie“ muss existieren, bevor die Pivot-Tabelle erstellt wird); Unterschied zwischen Funktion und Methode.

**Problem & Lösung:**
-Problem: Unter der neuen Überschrift wurde statt der Pivot-Tabelle die Monatsübersicht ausgegeben
-Lösung: Ursache war der Aufruf der alten Funktion `monatsuebersicht`, Aufruf auf `kategorien_pro_monat(df)` angepasst.


-> Die Auswertung nach Monat zeigt Abweichungen, die in der Gesamtsumme untergehen: Das Minus im August (−664,38 €) entsteht fast vollständig durch einen einzelnen Amazon-Einkauf über 649 € (Online Shopping −718,18 € statt sonst −185,91 € bzw. −21,64 €).

-> Auffälligkeit bei den Fixkosten: „Abos & Verträge“ liegt im September bei −60,96 € statt −49,97 €. Ursache ist eine doppelte Spotify-Abbuchung über 10,99 €.


**Nächster Schritt:**
Doppelbuchungen automatisch erkennen, damit Fehler wie die doppelte Spotify-Abbuchung nicht mehr manuell gesucht werden müssen.


