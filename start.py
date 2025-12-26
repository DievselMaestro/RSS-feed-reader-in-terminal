#!/usr/bin/env python3
from datetime import date
DatumHeute = date.today()
Dateiname = "demofile.txt"

Datei = open(Dateiname)
# Das heute Datum
print("Heute ist:",DatumHeute)
Datei.close()
print("-------")
zeile = 0
with open(Dateiname) as f:
    for x in f:
        zeile = zeile + 1
        print(zeile,":",x)

str(DatumHeute)
if DatumHeute == "":
    print("Datum ist nicht gesetzt")
else:
    print("Datum ist heute auf true")


"""
Funktion erstellen die checkt ob die Variable leer ist oder nicht
"""

def ist_variabel_leel(variabel):
    if variabel == "":
      print("Die Variabel:",variabel, "ist leer.")
    else:
        print("Die Variabel:",variabel, "ist nicht leer.")

print("Funktions test")
ist_variabel_leel(DatumHeute)

ist_variabel_leel(__name__)
print("main :",__name__)


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
