"""
Övning 2.13 - Uppdatera element i en lista
Skriv ett program som gör följande:
Skapa två listor, start_list = [5, 3, 1, 2, 4] och en tom lista  square_list = []
Kopiera värdena från  start_list till square_list.
Byt ut varje värde i square_list mot kvadraten på talet (talet upphöjt till 2).
Sortera värdena i square_list
Skriv ut square_list i terminalen.
"""

import math
import random


def is_sorted(num_list):
    last = -math.inf
    for i in num_list:
        if last > i:
            return False
        last = i
    return True


def swap(list, i1, i2):
    a = list[i2]
    list[i2] = list[i1]
    list[i1] = a


# om man har tur är denna sorten snabb
def bogosort(num_list):
    while not is_sorted(num_list):
        swap(num_list, random.randrange(len(num_list)), random.randrange(len(num_list)))


def square_list(num_list):
    for i in range(len(num_list)):
        num_list[i] = num_list[i] ** 2


l = [5, 6, 2, 8, 3, 4, 0, -23]
print(l)

print("Squaring...")
square_list(l)
print(l)
print("Sorting...")
bogosort(l)
print(l)