#!/usr/bin/env python3
import feedparser
from colorama import init, Fore, Back, Style
init(autoreset=True)

DEBUG_MODE: bool = True
DEFAULT_RSS_URL: str = "https://www.heise.de/rss/heise-atom.xml"
    
def prompt_input() -> str:
    """
    Fragt den Benutzer nach einer RSS-Feed-URL.
    Im Debug-Modus wird eine Standard-URL verwendet.

    Returns:
        str: Die RSS-Feed-URL
    """ 
    
    if DEBUG_MODE:
        rss_feed_url = DEFAULT_RSS_URL
    else:
        print("Enter RSS feed URL:")
        rss_feed_url = input()
        
    return str(rss_feed_url).strip()
               

def get_rss_feed() -> None:
    """
    RSS Feed abrufen und in der Console ausgeben.
    
    Returns:
        none
    """
    
    try:
        url = prompt_input()
        d = feedparser.parse(url)
        
        if not d.entries:
            print(f"Keine Einträge gefunden prüfe die RSS URL.")
            return
        
        for index, entry in enumerate(d.entries):
            # RSS feed
            print(f"{Style.BRIGHT}{Fore.YELLOW}RSS Feed: {index}")
            print()
            print(f"{Style.BRIGHT}{Fore.MAGENTA}Titel: {Style.NORMAL}{Fore.WHITE}{entry.title}")
            print(f"{Style.BRIGHT}{Fore.MAGENTA}Beschreibung: {Style.NORMAL}{Fore.WHITE}{entry.description}")
            print(f"{Style.BRIGHT}{Fore.MAGENTA}Link: {Style.NORMAL}{Fore.WHITE}{entry.link}")
            print(f"{Style.DIM}{Fore.BLUE}Datum: {Style.NORMAL}{Fore.BLUE}{entry.published}")
            print()
            print("------------------")
            print()
            
    except Exception as e:
        print(f"Fehler beim laden des RSS-Feeds: {e}")
        return
 
def main():
    get_rss_feed()


if __name__ == "__main__":
    main()

