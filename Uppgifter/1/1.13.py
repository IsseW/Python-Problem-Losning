"""
Övning 1.13 - Procent
Skriv en funktion  percent(value, total), som tar in två tal som argument och returnerar procentvärdet som ett heltal.

>>> percent(46, 90) 
51
>>> percent(51, 51) 
100
>>> percent(63, 12) 
525
"""


def percent(value, total):
    return int(100 * value / total)


print(str(percent(float(input("Value: ")), float(input("Total: ")))) + "%")