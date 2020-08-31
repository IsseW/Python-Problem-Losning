"""
Övning 1.7 - Hur många timmar, minuter och sekunder?
Skriv ett program som ser ut så här när det kör.
Kursiv stil innebär att användaren matar in.

How many seconds? 4000

4000 seconds are 1 hours, 6 minutes and 40 seconds
"""

s = int(input("How many seconds? "))

m = s // 60
sec = s - m * 60
hours = m // 60
min = m - hours * 60

print(
    str(s)
    + " seconds are "
    + str(hours)
    + " hours, "
    + str(min)
    + " minutes and "
    + str(sec)
    + " seconds."
)
