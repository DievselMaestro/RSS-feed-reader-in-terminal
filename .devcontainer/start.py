#!/usr/bin/env python3
Dateiname = "demofile.txt"

Datei = open(Dateiname)
print(Datei.read())
Datei.close()
print("-------")
zeile = 0
with open(Dateiname) as f:
    for x in f:
        zeile = zeile + 1
        print(zeile":"x)



"""
with open("demofile.txt") as f:
  print(f.readline())

with open("demofile.txt") as f:
  for x in f:
    print(x)

"""


""" Beispiel 
f = open("demofile.txt")
print(f.read())
"""
