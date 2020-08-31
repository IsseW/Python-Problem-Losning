"""
Övning 1.23 - Gissa talet I
Skriv ett program som slumpar ett tal (se koden nedan för slumpning av tal), sedan får användaren gissa vilket tal som slumpades fram.

import random

#slumptal ur motsvarande range(), slumpar i detta fall i intervallet 0..99
random1 = random.randrange(100)  

#slumptal ur intervallet 1..100
random2 = random.randint(1, 100) 
För att användaren ska få en ärlig chans att gissa rätt så slumpa tal mellan 1 och 10. Programmet ska meddela om gissningen var rätt eller inte.
Variera ditt program:
Slumpa tal i intervallet 1..5 istället.
Slumpa tal i intervallet 2..6 istället.
Låt användaren mata in min- och maxgräns för det slumpade talet. 
"""

import random

min = int(input("Min: "))
max = int(input("Max: "))

random = random.randint(min, max)


while (
    not int(input("Gissa ett tal mellan " + str(min) + " och " + str(max) + ": "))
    == random
):
    print("Fel!")

print("Rätt!")
