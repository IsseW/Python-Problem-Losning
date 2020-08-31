"""
Övning 1.20 - Maximum, version 2
Definiera en funktion max3(num1, num2, num3) som tar in 3 tal som parametrar och returnerar största av dem.
När funktionen körs från Python-terminalen ska det se ut så här:

>>> max3(3, 7, 9)
9
>>> max3(1, 3, 2)
3
"""


def max3(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        return num3
    if num2 > num3:
        return num2
    return num3


print("Max: " + str(max3(int(input("A: ")), int(input("B: ")), int(input("C: ")))))