"""
Övning 1.4 - Omvandla enheter
Skriv ett Python-program som beräknar följande:

Hur många sekunder är 45 minuter och 20 sekunder?
Hur många miles blir 20 kilometer?
Tips! En mile är 1,609344 km.
"""

min = 45
sec = 20

t = min * 60 + sec

print(str(min) + " minuter och " + str(sec) + " sekunder blir " + str(t) + " sekunder")

km = 20

miles = km * 1.609344

print(str(km) + " km är " + str(miles) + " miles")
