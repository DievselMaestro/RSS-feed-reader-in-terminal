#!/usr/bin/env python3
import feedparser
from colorama import init, Fore, Back, Style
init(autoreset=True)

# Funktion für die Eingabe der URL anfragen
def prompt_input() -> str: 
    # Debug On or Off
    var_debug_on: bool = True
    if var_debug_on:
        rss_feed_url: str = "https://www.heise.de/rss/heise-atom.xml"
    else:
        print("Enter RSS feed URL:")
        rss_feed_url = input()
        
    return str(rss_feed_url).strip()
               

def get_rss_feed() -> None:
    # RSS von der URL Adresse abrufen
    
    # print(d.feed.title_detail)
    
    try:
        url = prompt_input()
        d = feedparser.parse(url)
        
        if not d.entries:
            print(f"Keine Einträge gefunden prüfe die RSS URL.")
            return
        
        for index, entry in enumerate(d.entries):
            # RSS feed
            print(f"{Style.BRIGHT}{Fore.YELLOW}RSS Feed: {index}")
            print("")
            print(f"{Style.BRIGHT}{Fore.MAGENTA}Titel: {Style.NORMAL}{Fore.WHITE}{entry.title}")
            print(f"{Style.BRIGHT}{Fore.MAGENTA}Beschreibung: {Style.NORMAL}{Fore.WHITE}{entry.description}")
            print(f"{Style.BRIGHT}{Fore.MAGENTA}Link: {Style.NORMAL}{Fore.WHITE}{entry.link}")
            print(f"{Style.DIM}{Fore.BLUE}Datum: {Style.NORMAL}{Fore.BLUE}{entry.published}")
            print("")
            print("------------------")
            print("")
            
    except Exception as e:
        print(f"Fehler beim laden des RSS-Feeds: {e}")
        return
 
def main():
    get_rss_feed()


if __name__ == "__main__":
    main()

