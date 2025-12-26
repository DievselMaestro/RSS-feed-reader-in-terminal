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
    print("Enter RSS feed URL")
    rss_feed_url = input()
    return (rss_feed_url)

def get_rss_feed():
    d = feedparser.parse(prompt_input())
    print(d.feed.title_detail)



def main():
    get_rss_feed()

#var = prompt_input()


#test = input()

#is_var_empty(var)

if __name__ == "__main__":
    main()

print(__name__)