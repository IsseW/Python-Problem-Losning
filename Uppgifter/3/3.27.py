"""
Övning 3.27 - Summera alla tal från ett
Skriv en rekursiv funktion sum_all(int_num) som tar in ett tal och summerar alla positiva tal upp till och med det givna talet.
Körexempel:

>>> sum_all(5)
15 

>>> sum_all(-10)
'Invalid'

>>> sum_all(10)
55
"""


def sum_all(int_num):
    if int_num < 0:
        return "Invalid"
    return 0 if int_num == 0 else int_num + sum_all(int_num - 1)


print(sum_all(5))
print(sum_all(-10))
print(sum_all(10))