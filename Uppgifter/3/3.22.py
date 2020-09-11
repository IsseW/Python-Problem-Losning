"""
Övning 3.22 - Största gemensamma delare (Greatest Common Divisor)
Största gemensamma delare av två eller flera nollskilda heltal är det största positiva heltal som delar talen med heltalskvot utan att ge någon rest. 
Skriv en rekursiv funktion gcd(a, b) 
för att bestämma största gemensamma delare för två heltal genom att använda Euklides algoritm (a > b):
Körexempel:

>>> gcd(84, 18)
6

>>> gcd(112, 42)
14 

>>> gcd(5, 4)
1
"""


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


print(gcd(84, 18))
print(gcd(112, 42))
print(gcd(5, 4))
