# Entwicklungstagebuch

## Tag 1 – 20.10.2026
**Erledigt:** Projektstruktur angelegt, fiktiven Kontoauszug (62 Buchungen, Juli–September 2026) erstellt, Skript zum Einlesen und für die Monatsübersicht geschrieben, Projekt auf GitHub hochgeladen.

**Gelernt:** Grundlagen von Git und GitHub (Repository, Commit, Push, privates vs. öffentliches Repository); deutsche CSV-Formate (Semikolon, Dezimalkomma) mit pandas einlesen.

**Problem & Lösung:** Erste Commit-Version enthielt persönliche Arbeitsnotizen. Lösung: Repository neu aufgesetzt und Inhalte sauber getrennt (öffentliche Projektdateien vs. private Notizen).

**Nächster Schritt:** Händler automatisch in Kategorien einordnen (Tag 2).

## Tag 2 – 21.10.2026
**Erledigt:**
Kategorien angesetzt, Ausgaben werden jetzt sinnvoll kategorisiert -> Übersichtlichkeit

Die ersten zwei Kategorien waren vorgegeben, die übrigen habe ich selbst ergänzt, sodass keine Buchung mehr unter „Sonstiges“ fällt.

Kategorien anschließend überarbeitet: Fixkosten in „Abos & Verträge“ zusammengefasst, Gesundheit separat, Bezeichnungen vereinheitlicht (z. B. „Mobilität“, „Mobilfunk“).

**Gelernt:**
Python lokal installieren und Bibliotheken mit pip verwalten; Dictionaries in Python; Funktionen aus einer eigenen Datei importieren; Suchbegriffe präzise wählen (z. B. „dm-drogerie“ statt „dm“, um Fehlzuordnungen zu vermeiden).

**Problem & Lösung:**
- Problem: Zu viele Umsätze -> schwer alles zuzuordnen und ist unübersichtlich
- Lösung: Durch Kategorien schafft man es die Umsätze besser im Blick zu behalten.


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
- Problem: Unter der neuen Überschrift wurde statt der Pivot-Tabelle die Monatsübersicht ausgegeben
- Lösung: Ursache war der Aufruf der alten Funktion `monatsuebersicht`, Aufruf auf `kategorien_pro_monat(df)` angepasst.


-> Die Auswertung nach Monat zeigt Abweichungen, die in der Gesamtsumme untergehen: Das Minus im August (−664,38 €) entsteht fast vollständig durch einen einzelnen Amazon-Einkauf über 649 € (Online Shopping −718,18 € statt sonst −185,91 € bzw. −21,64 €).

-> Auffälligkeit bei den Fixkosten: „Abos & Verträge“ liegt im September bei −60,96 € statt −49,97 €. Ursache ist eine doppelte Spotify-Abbuchung über 10,99 €.


**Nächster Schritt:**
Doppelbuchungen automatisch erkennen, damit Fehler wie die doppelte Spotify-Abbuchung nicht mehr manuell gesucht werden müssen.

## Tag 4 – 24.10.2026
**Erledigt:**
Code nach dem DRY-Prinzip überarbeitet: Die Spalte `monat` wird jetzt einmalig in `kontoauszug_laden` erzeugt statt doppelt in `monatsuebersicht` und `kategorien_pro_monat` -> eine zentrale Stelle für Änderungen, Ausgabe unverändert

Neue Funktion `doppelbuchungen_finden`: Buchungen mit gleichem Text, Betrag und Monat werden als Verdacht auf Doppelbuchung ausgegeben -> doppelte Spotify-Abbuchung im September wird automatisch erkannt

**Gelernt:**
DRY-Prinzip (Don't Repeat Yourself); Refactoring: Code verbessern, ohne das Ergebnis zu verändern (Kontrolle über identische Ausgabe vorher/nachher); Funktionen erhalten dasselbe DataFrame und keine Kopie, Änderungen darin wirken sich auf das Original aus (Seiteneffekte).

`duplicated` mit `subset` und `keep=False` (alle betroffenen Buchungen markieren, nicht nur die zweite); Filtern eines DataFrames über True/False-Werte; Auswahl mehrerer Spalten mit `[[...]]`.

**Problem & Lösung:**
- Problem: Erste Version lieferte 38 statt 2 Treffer, darunter viele normale Einkäufe mit unterschiedlichen Beträgen
- Lösung: Ursache anhand der Ausgabe erkannt (unterschiedliche Beträge wurden als doppelt markiert, einmalige Monatsbuchungen wie die Miete fehlten) -> `betrag` fehlte im Vergleich, `subset` auf `["text", "betrag", "monat"]` korrigiert.


-> Designentscheidung: Auswertungsfunktionen arbeiten ohne `df.copy()`, da sie die Daten nur lesen und nicht verändern. Eine Kopie würde bei großen Datenmengen (z. B. Millionen Buchungen in einem Unternehmen) unnötig Speicher und Rechenzeit verbrauchen. Kopiert wird nur, wenn eine Funktion Daten tatsächlich verändert.

-> Ein Treffer ist nur ein Verdacht und kein sicherer Fehler: Zwei gleiche Bahntickets im selben Monat wären z. B. legitim. Das Programm markiert, ein Mensch prüft.

**Nächster Schritt:**
Ungewöhnlich hohe Ausgaben automatisch erkennen, damit Ausreißer wie der Amazon-Einkauf über 649 € im August nicht mehr manuell gesucht werden müssen.

## Tag 5 – 25.10.2026
**Erledigt:**
Neue Funktion `ausreisser_finden`: Ausgaben werden als ungewöhnlich hoch markiert, wenn sie mehr als das Dreifache des Medians ihrer Kategorie betragen -> Amazon-Einkauf über 649 € im August wird automatisch erkannt, ohne Fehlalarme

Grenzwert relativ zur Kategorie statt fester Betrag: Ein fester Grenzwert (z. B. 200 €) würde die Miete jeden Monat markieren und ungewöhnliche Beträge in günstigen Kategorien (z. B. Lebensmittel) übersehen.

**Gelernt:**
Median vs. Mittelwert: Der Median ist robust gegenüber Ausreißern, der Mittelwert nicht (Online Shopping: Mittelwert −154,29 €, Median −66,47 €); `transform` liefert im Gegensatz zu `agg` für jede Buchung den Wert ihrer Gruppe und ermöglicht so den Vergleich Zeile für Zeile.

Zeilen filtern nach dem Muster `tabelle[bedingung]`; Standardwerte für Parameter (`faktor = 3`), damit der Grenzwert sichtbar und anpassbar ist statt als feste Zahl im Code; Vergleiche bei negativen Beträgen: höhere Ausgabe = kleinerer Wert.

**Problem & Lösung:**
- Problem: Erster Ansatz mit Mittelwert und Standardabweichung war instabil, da der Ausreißer beide Werte selbst stark verzerrt (bei 2,5 Standardabweichungen wurde der Amazon-Einkauf nicht mehr erkannt)
- Lösung: Umstieg auf den Median der jeweiligen Kategorie als Referenzwert.


-> Wahl des Faktors getestet: Faktor 2 markiert zusätzlich zwei normale Wocheneinkäufe bei REWE (ca. 69 €) als auffällig, Faktor 3 findet nur den tatsächlichen Ausreißer.

-> Mögliche Erweiterung: Wesentlichkeitsgrenze relativ zum Einkommen, damit nur Beträge markiert werden, die finanziell tatsächlich ins Gewicht fallen.


**Nächster Schritt:**
Code und README aufräumen, unter anderem eine Beispielausgabe in die README aufnehmen, damit die Funktionen ohne Ausführen des Programms sichtbar sind.

## Tag 6 – 25.10.2026
**Erledigt:**
Kategorie-Auswertungen auf Ausgaben beschränkt: Das Einkommen erscheint nicht mehr in „Ausgaben nach Kategorie“ und „Ausgaben nach Kategorie und Monat“ -> Überschrift und Inhalt stimmen überein, Monatsübersicht mit Einnahmen und Saldo bleibt unverändert

Neue Funktion `nur_ausgaben` als zentrale Filterregel, die sowohl in `main` als auch in `ausreisser_finden` verwendet wird.

**Gelernt:**
DRY bezieht sich auf die Definition einer Regel, nicht auf die Anzahl ihrer Aufrufe: Die Regel „Ausgabe = negativer Betrag“ ist einmal definiert und wird an mehreren Stellen genutzt; die Position eines Filters entscheidet über das Ergebnis.

Funktionen sollten sich nicht darauf verlassen, bereits korrekt gefilterte Daten zu erhalten, sondern selbst sicherstellen, dass sie mit den richtigen Daten arbeiten.

**Problem & Lösung:**
- Problem: Die Auswertungen mit der Überschrift „Ausgaben“ enthielten auch das Einkommen (+1.150 € pro Monat) und waren dadurch irreführend
- Lösung: Abwägung zwischen Umbenennen der Überschriften und Herausfiltern des Einkommens, Entscheidung für den Filter, da bei der Analyse die Ausgaben im Fokus stehen.


-> Den Filter global in `kontoauszug_laden` zu setzen hätte die Monatsübersicht verfälscht (Einnahmen 0 €, falscher Saldo).

-> Den Filter nur einmal in `main` anzuwenden hätte `ausreisser_finden` abhängig von vorgefilterten Daten gemacht: Bei einem Aufruf mit allen Buchungen wäre das Gehalt als ungewöhnlich hohe Ausgabe markiert worden.


**Nächster Schritt:**
Beispielausgabe in die README aufnehmen, damit die Funktionen ohne Ausführen des Programms sichtbar sind.