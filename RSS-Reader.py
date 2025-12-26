#!/usr/bin/env python3
import feedparser

# Check is the Variabel is empty or not
# for Debug reason
def is_var_empty(var):
    if var == "":
        print("The Var:",var,"is empty!")
    else:
        print("The Var:",var,"is not empty!")

# Funktion für die Eingabe der URL anfragen
def prompt_input():
    print("Enter RSS feed URL")
    rss_feed_url = input()
    return (rss_feed_url)


var = prompt_input()


#test = input()

is_var_empty(var)