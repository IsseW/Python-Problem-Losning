"""
Övning 3.20 - Upphöjt
Skriv en rekursiv funktion power(base, exp) där exp är ett heltal för att räkna ut värdet av
base upphöjt till exp.
Körexempel:

>>> power(5, 2)
25

>>> power(5, 1)
5 

>>> power(5, 0)
1
"""


def power(base, exp):
    return 1 if exp == 0 else base * power(base, exp - 1)


print(power(5, 2))
print(power(5, 1))
print(power(5, 0))