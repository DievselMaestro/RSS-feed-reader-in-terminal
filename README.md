# RSS Feed Reader Terminal

Ein Python-basierter RSS-Feed-Reader für die Kommandozeile mit farbiger Ausgabe.

## Beschreibung

Dieses Programm ermöglicht es, RSS-Feeds direkt im Terminal zu lesen. Es unterstützt sowohl einzelne URLs als auch mehrere URLs aus einer Datei.

## Voraussetzungen

- Python 3.12 oder höher
- Benötigte Python-Pakete:
  - `feedparser` - Zum Parsen von RSS-Feeds
  - `colorama` - Für farbige Terminal-Ausgabe

## Installation

```bash
pip install feedparser colorama
```

## Verwendung

```bash
python RSS-Reader.py
```

Das Programm fragt dich, ob du eine einzelne URL oder mehrere URLs aus einer Datei abrufen möchtest.

### Einzelne URL
- Wähle "N" oder "Nein"
- Gib die RSS-Feed-URL ein

### Mehrere URLs
- Wähle "J" oder "Ja"
- Das Programm liest URLs aus der Datei `RSS-Feed-URL.txt`
- Jede URL muss in einer separaten Zeile stehen

## Code-Struktur

### Konstanten

```python
DEBUG_MODE: bool = False
DEFAULT_RSS_URL: str = "https://www.heise.de/rss/heise-atom.xml"
FILE_NAME: str = "RSS-Feed-URL.txt"
```

- `DEBUG_MODE`: Aktiviert den Debug-Modus (verwendet Standard-URL)
- `DEFAULT_RSS_URL`: Standard-RSS-Feed für den Debug-Modus
- `FILE_NAME`: Dateiname für die Liste der RSS-Feed-URLs

### Funktionen

#### `open_file() -> list`

Öffnet die Datei `RSS-Feed-URL.txt` und liest alle URLs.

**Rückgabewert:**
- Liste mit URLs (jede Zeile wird mit `.strip()` von Leerzeichen und Newline-Zeichen befreit)

**Beispiel Dateiinhalt:**
```
https://www.heise.de/rss/heise-atom.xml
https://feedparser.readthedocs.io/en/latest/examples/rss20.xml
```

**Fehlerbehandlung:**
- Bei Fehlern wird eine Fehlermeldung ausgegeben

#### `prompt_input() -> list`

Fragt den Benutzer nach der Eingabemethode (einzelne URL oder mehrere URLs).

**Rückgabewert:**
- Liste mit einer oder mehreren URLs

**Ablauf:**
1. Fragt: "Wollen sie mehrere RSS Feed URL abrufen? Ja oder Nein? J/N:"
2. Bei "Nein"/"N": Fragt nach einer einzelnen URL und gibt sie als Liste zurück `[url]`
3. Bei "Ja"/"J": Ruft `open_file()` auf und gibt die Liste der URLs zurück
4. Bei ungültiger Eingabe: Wiederholt die Frage

**Debug-Modus:**
- Wenn `DEBUG_MODE = True`, wird automatisch die `DEFAULT_RSS_URL` verwendet

#### `get_rss_feed() -> None`

Hauptfunktion zum Abrufen und Anzeigen der RSS-Feeds.

**Ablauf:**
1. Ruft `prompt_input()` auf, um URLs zu erhalten
2. Iteriert über alle URLs
3. Parst jeden RSS-Feed mit `feedparser.parse(url)`
4. Zeigt bis zu 6 Einträge pro Feed an
5. Bricht nach dem 6. Eintrag ab

**Angezeigte Informationen:**
- RSS Feed Index und Hostname (z.B. "RSS Feed: 0 --- www.heise.de")
- Titel des Artikels
- Beschreibung
- Link zum Artikel
- Veröffentlichungsdatum

**Farbschema:**
- Gelb (YELLOW + BRIGHT): RSS Feed Index
- Magenta (MAGENTA + BRIGHT): Feldnamen (Titel, Beschreibung, Link)
- Weiß (WHITE): Feldwerte
- Blau (BLUE): Datum

**Fehlerbehandlung:**
- Wenn keine Einträge gefunden werden: Fehlermeldung und Abbruch
- Bei Parsing-Fehlern: Fehlermeldung wird ausgegeben

#### `get_name_from_url(var: int, url) -> str`

Extrahiert den Hostnamen aus einer URL.

**Parameter:**
- `var`: Index (wird aktuell nicht verwendet)
- `url`: Die vollständige URL

**Rückgabewert:**
- Hostname der URL (z.B. "www.heise.de")

**Beispiel:**
```python
url = "https://www.heise.de/rss/heise-atom.xml"
hostname = get_name_from_url(0, url)
# Ergebnis: "www.heise.de"
```

**Verwendete Methode:**
- `urlparse(url).hostname` aus dem Modul `urllib.parse`

#### `main()`

Einstiegspunkt des Programms. Ruft `get_rss_feed()` auf.

## Beispielausgabe

```
Wollen sie mehrere RSS Feed URL abrufen? Ja oder Nein? J/N: N
Enter RSS feed URL:
https://www.heise.de/rss/heise-atom.xml

RSS Feed: 0 --- www.heise.de

Titel: Beispiel-Artikel
Beschreibung: Dies ist eine Beispiel-Beschreibung
Link: https://www.heise.de/artikel/123456
Datum: Mon, 03 Jan 2026 10:00:00 GMT

--------------------
```

## Dateiformat für RSS-Feed-URL.txt

Erstelle eine Textdatei mit dem Namen `RSS-Feed-URL.txt` im gleichen Verzeichnis wie das Programm:

```
https://www.heise.de/rss/heise-atom.xml
https://feedparser.readthedocs.io/en/latest/examples/rss20.xml
```

Jede URL muss in einer separaten Zeile stehen.

## Limitierungen

- Maximal 6 Einträge pro RSS-Feed werden angezeigt
- Bei mehreren URLs werden alle nacheinander abgerufen (keine parallele Verarbeitung)

## Technische Details

### Verwendete Module

1. **feedparser**: RSS/Atom Feed Parser
   - `feedparser.parse(url)` gibt ein Dictionary-ähnliches Objekt zurück
   - Zugriff auf Einträge über `d.entries`

2. **colorama**: Cross-Platform Terminal-Farben
   - `init(autoreset=True)`: Setzt Farben nach jedem print() zurück
   - `Fore`: Vordergrundfarben (YELLOW, MAGENTA, WHITE, BLUE)
   - `Style`: Text-Stile (BRIGHT, NORMAL, DIM)

3. **urllib.parse**: URL-Parsing
   - `urlparse(url)`: Zerlegt URL in Komponenten
   - `.hostname`: Extrahiert nur den Hostnamen

## Lizenz

Dieses Projekt ist Open Source.
