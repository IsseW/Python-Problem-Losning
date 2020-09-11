"""
Övning 3.32 - ☆☆ Pascals triangel
Pascals triangel formas genom att man fyller de två översta raderna med ettor. Alla siffror på kanterna sätts till 
1. Varje element inuti triangeln är summan av de två element som står ovanför. 
Skriv en rekursiv funktion pascal(k, i)som beräknar ett värde ur Pascals triangel 
givet rad k och kolumn i. 


Körexempel:
>>> pascal(0, 0)   # top element
1

>>> pascal(2, 0)  
1

>>> pascal(4, 2)   # (4, 2) = (3, 1) + (3 , 2)
6

>>> pascal(5, 3)   # (5, 3) = (4, 2) + (4, 3)
10

>>> pascal(3, 5) 
'Invalid input combination'
"""


def pascal(k, i):
    if i < 0 or k < 0 or k > 6 or i > k:
        return "Invalid Position"
    if k == i or i == 0:
        return 1
    return pascal(k - 1, i - 1) + pascal(k - 1, i)


print(pascal(0, 0))
print(pascal(2, 0))
print(pascal(4, 2))
print(pascal(5, 3))
print(pascal(3, 5))