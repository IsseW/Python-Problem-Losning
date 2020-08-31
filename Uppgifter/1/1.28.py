"""
Övning 1.28 - Skriv om if-sats
Skriv om nedanstående if-sats utan att använda nästling (if-sats inne i en if-sats).
Ledning: För vilka värden på n skrivs de olika meddelandena ut? 

if n > 0:
    if n > 100:
        print('Big!')
    else:
        if n <= 50:
            print('Medium')
        else:
            print('A little larger')
else:
    print('Tiny') ) 
"""

n = int(input("Write a number: "))

if n < 0:
    print('Tiny')
elif n <= 50:
    print('Medium')
elif n <= 100:
    print('A little larger')
else:
    print("Big!")
