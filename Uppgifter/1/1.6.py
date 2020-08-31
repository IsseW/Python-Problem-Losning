"""
Övning 1.6 - Hur gammal är du? 
Skriv ett program som ser ut så här när det kör.
Kursiv stil innebär att användaren matar in.

What year were you born? 1973
What month? March
What day? 28

OK, then you will turn 46 on March 28 in 2019!
☆ Utmaning: Använd funktionen time() i modulen time för att beräkna hur många år och dagar gammal personen är med hjälp av samma inmatade information som ovan.
Ett anrop till time.time() returnerar hur många sekunder som passerat sedan 1 januari 1970 (GMT).
OBS! Använd månadens nummer istället för text i den här varianten, så att det går att räkna ut!
"""


import time
from datetime import datetime

year = int(input("What year were you born? "))

month = input("What month were you born? ")

day = int(input("What day were you born? "))

age = 2020 - year

print("You will turn " + str(age) + " on " + month + " " + str(day) + " in 2020")

month_num = datetime.strptime(month, "%B").month

t = time.time() - datetime(year, month_num, day).timestamp()

print("You are " + str(t) + " seconds old")
# Could use integer divide '//' but who cares
print(str(t / 60) + " minutes old")
print(str(t / 3600) + " hours old")
print(str(t / (3600 * 24)) + " days old")
print(str(t / (3600 * 24 * 365)) + " years old")