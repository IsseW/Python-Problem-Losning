"""
Övning 2.14 - Summera tal
Skriv en funktion sum_numbers(any_list) som summerar alla element i listan som är tal och returnerar summan. Alla list-element som inte är tal ska ignoreras.
Kodsnutten nedan visar hur man kan göra en funktion som kontrollerar om något är ett tal eller inte:
import numbers

def is_number(item):
    return isinstance(item, numbers.Number)


Returvärdet från is_number() kommer att vara True om argumentet är ett tal och False i annat fall. Nu kan du kontrollera om något är ett tal genom att göra ett anrop likt is_number(5.324).

När funktionen sum_numbers() används ska det kunna se ut så här:
 
>>> sum_numbers([1, 2, 3.2, 4, 5 ])
15.2
>>> sum_numbers([’a’, 1, ’b’, 2, [[’b’, 4], 2], 3])
6
"""

import numbers


def is_number(item):
    return isinstance(item, numbers.Number)


def sum_numbers(list):
    sum = 0
    for i in list:
        if is_number(i):
            sum += i
    return sum


print(sum_numbers([1, 2, 3.2, 4, 5]))
print(sum_numbers(["a", 1, "b", 2, [["b", 4], 2], 3]))