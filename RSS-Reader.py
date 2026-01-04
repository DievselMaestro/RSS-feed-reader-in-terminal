#!/usr/bin/env python3
import feedparser
from urllib.parse import urlparse
from colorama import init, Fore, Back, Style
init(autoreset=True)

DEBUG_MODE: bool = False
DEFAULT_RSS_URL: str = "https://www.heise.de/rss/heise-atom.xml"
FILE_NAME: str = "RSS-Feed-URL.txt"

def open_file() -> list:
    """
    öffne die Datei
    
    :return: gibt den inhalt der Datei zurück
    :rtype: list
    """
    try:
        with open(FILE_NAME, "r") as file:
            a = [line.strip() for line in file]
            print(f"Datei Inhalt: {a}")
            return a
    except Exception as e:
        print(f"Fehler beim öffnen der Datei {e}")
        
def prompt_input():
    """
    Fragt den Benutzer nach einer RSS-Feed-URL.
    Im Debug-Modus wird eine Standard-URL verwendet.

    Returns:
        str: Die RSS-Feed-URL
    """ 
     
    if DEBUG_MODE:
        rss_feed_url = DEFAULT_RSS_URL
    else:
        while True:
            user_input = input("Wollen sie mehrere RSS Feed URL abrufen? Ja oder Nein? J/N: ")

            if user_input.lower() in ["Nein", "n"]:
                print("Enter RSS feed URL:")
                rss_feed_url = input()
                return [rss_feed_url.strip()]
            elif user_input.lower() in ["Ja", "j"]:
                return open_file()
            else:
                print(f"Invalid input. Please enter ja/nein.")   

def get_rss_feed() -> None:
    """
    RSS Feed abrufen und in der Console ausgeben.
    Bis maximal 6 wiederholungen.
    
    Returns:
        none
    """
    
    try:
        
        urls = prompt_input()
        print(f"urls: {urls}")
        for url in urls:
            d = feedparser.parse(url)
            
            if not d.entries:
                print(f"Keine Einträge gefunden prüfe die RSS URL.")
                return
            
            for index, entry in enumerate(d.entries):
                # RSS feed
                print(f"{Style.BRIGHT}{Fore.YELLOW}RSS Feed: {index} --- {get_name_from_url(index,url)}")
                print()
                print(f"{Style.BRIGHT}{Fore.MAGENTA}Titel: {Style.NORMAL}{Fore.WHITE}{entry.title}")
                print(f"{Style.BRIGHT}{Fore.MAGENTA}Beschreibung: {Style.NORMAL}{Fore.WHITE}{entry.description}")
                print(f"{Style.BRIGHT}{Fore.MAGENTA}Link: {Style.NORMAL}{Fore.WHITE}{entry.link}")
                print(f"{Style.DIM}{Fore.BLUE}Datum: {Style.NORMAL}{Fore.BLUE}{entry.published}")
                print()
                print("-" * 20)
                print()
                
                # Bricht Loop nach der 6 wiederholung ab
                if index == 5:
                    break
            
    except Exception as e:
        print(f"Fehler beim laden des RSS-Feeds: {e}")
        return
    
    
def get_name_from_url(var:int,url) -> str:
    """
    Extrahiert den Hostnamen aus einer RSS-Feed-URL.

    Beispiel: "https://www.heise.de/rss/heise-atom.xml" -> "www.heise.de"

    :param var: Index des RSS-Feeds (aktuell nicht verwendet)
    :type var: int
    :param url: Die vollständige RSS-Feed-URL
    :type url: str
    :return: Der Hostname der URL (z.B. "www.heise.de")
    :rtype: str
    """
    o = urlparse(url)
    return o.hostname
        
    
 
def main():
    get_rss_feed()



if __name__ == "__main__":
    main()

