"""
Övning 1.15 - Ental och tiotal
Definiera två olika funktioner  unit(int_num) och  ten(int_num)  som returnerar entalssiffran respektive tiotalssiffran i ett heltal int_num.
När funktionerna körs i en Python-terminal ska det se ut så här:

>>> unit(123) 
3
>>> ten(123) 
2
"""


def get_unit(int_num: int, place: int):
    s = str(int_num)
    if place >= len(s):
        return 0
    return int(s[len(s) - 1 - place])


def unit(int_num: int):
    return get_unit(int_num, 0)


def ten(int_num: int):
    return get_unit(int_num, 1)


num = int(input("Number: "))
place = int(input("Place: ")) - 1
if place >= 0:
    print(
        "The "
        + str(place + 1)
        + "th place in the number "
        + str(num)
        + " is "
        + str(get_unit(num, place))
    )
