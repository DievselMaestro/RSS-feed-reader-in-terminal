#!/usr/bin/env python3
import feedparser
from colorama import init, Fore, Back, Style
init(autoreset=True)

# Check is the Variabel is empty or not
# for Debug reason
# def is_var_empty(var):
#     if var == "":
#         print("The Var:",var,"is empty!")
#     else:
#         print("The Var:",var,"is not empty!")
#         var_is_not_empty = True
#         return(var_is_not_empty)

# Funktion für die Eingabe der URL anfragen
def prompt_input():
    # Debug On or Off
    var_debug_on: bool = True
    if var_debug_on:
        rss_feed_url: str = "https://www.heise.de/rss/heise-atom.xml"
    else:
        print("Enter RSS feed URL:")
        rss_feed_url = input()
        
    return str(rss_feed_url).strip()
               

def get_rss_feed():
    # RSS von der URL Adresse abrufen
    d = feedparser.parse(prompt_input())
    # print(d.feed.title_detail)
    
    
    for index, entry in enumerate(d.entries):
        # RSS feed
        print(Style.BRIGHT + Fore.YELLOW + "RSS Feed:",index)
        print("")
        print(Style.BRIGHT + Fore.MAGENTA + "Titel: ",entry.title)
        print(Style.BRIGHT + Fore.MAGENTA + "Beschreibung:",entry.description)
        print(Style.BRIGHT + Fore.MAGENTA + "Link:", entry.link)
        print(Style.DIM + Fore.BLUE + "Datum:", Fore.BLUE + entry.published)
        print("")
        print("------------------")
        print("")
 
def main():
    get_rss_feed()

#var = prompt_input()


#test = input()

#is_var_empty(var)

if __name__ == "__main__":
    main()

#print(__name__)