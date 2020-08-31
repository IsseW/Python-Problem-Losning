"""
Övning 1.19 - Maximum
Definiera en funktion max2(num1, num2) som returnerar det största av de två talen  num1 och num2 givna som parametrar.
När funktionen körs från Python-terminalen ska det se ut så här:

>>> max2(8, 2)
8
"""


def max2(num1, num2):
    if num1 > num2:
        return num1
    return num2


print("Max: " + str(max2(int(input("A: ")), int(input("B: ")))))
