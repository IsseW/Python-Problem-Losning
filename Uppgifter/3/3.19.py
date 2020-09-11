"""
Övning 3.19 - Fakultet
En funktion som man vanligtvis implementerar rekursivt är fakultetsberäkning.
Fakultet av ett tal n är talet multiplicerat med fakultet av (n -1).
Fakultet av 0 är definierat som 1.

Skriv en rekursiv funktion i Python som beräknar och returnerar resultatet för fakultet av det tal som skickas in som argument.

Körexempel:

>>> factorial(5)
120

>>> factorial(1)
1

>>> factorial(0)
1
"""


def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)


print(factorial(5))
print(factorial(1))
print(factorial(0))