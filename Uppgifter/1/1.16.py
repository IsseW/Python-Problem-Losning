"""
Övning 1.16 - Byt plats på ental och tiotal
Definiera en funktion swap_units_and_tens(int_num),som byter plats på ordningen mellan tiotalssiffran och entalssiffran i talet och returnerar resultatet.
Du ska anropa de två funktionerna från föregående uppgift. När funktionen körs i Python-terminalen ska det se ut så här:

>>> swap_units_and_tens(123) 
132
"""


def swap_units_and_tens(int_num):
    negative = int_num < 0
    if negative:
        int_num = -int_num
    if int_num == 0:
        return 0
    s = list(str(int_num))
    if len(s) == 1:
        i = int(str(int_num) + "0")
        if negative:
            return -i
        return i
    ten = s[len(s) - 2]
    s[len(s) - 2] = s[len(s) - 1]
    s[len(s) - 1] = ten
    i = int("".join(s))
    if negative:
        return -i
    return i


print(str(swap_units_and_tens(int(input("Number: ")))))