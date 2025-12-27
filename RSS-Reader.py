#!/usr/bin/env python3
import feedparser

# Check is the Variabel is empty or not
# for Debug reason
def is_var_empty(var):
    if var == "":
        print("The Var:",var,"is empty!")
    else:
        print("The Var:",var,"is not empty!")
        var_is_not_empty = True
        return(var_is_not_empty)

# Funktion für die Eingabe der URL anfragen
def prompt_input():
    #Debug On or Off
    var_debug_on = 0
    if var_debug_on == 1:
        rss_feed_url = "https://www.heise.de/rss/heise-atom.xml"
    else:
        print("Enter RSS feed URL:")
        rss_feed_url = input()
        
    return rss_feed_url
               

def get_rss_feed():
    # RSS von der URL Adresse abrufen
    d = feedparser.parse(prompt_input())
    # print(d.feed.title_detail)
    
    i = 0
    for x in d.entries:
        #print(x)
        # RSS feed
        print("RSS Feed:",i)
        print("")
        print("Titel: ",d.entries[i].title)
        print("Link:", d.entries[i].link)
        print("Beschreibung:",d.entries[i].description)
        print("------------------")
        print("")
        i = i + 1
        #print("Datum:", d.feed.published)
        

def main():
    get_rss_feed()

#var = prompt_input()


#test = input()

#is_var_empty(var)

if __name__ == "__main__":
    main()

#print(__name__)