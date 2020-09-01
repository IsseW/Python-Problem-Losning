"""
Övning 2.17 - Summera första och sista
Skriv en funktion add_first_and_last(num_list) som tar in en lista med tal och summerar det första och det sista talet i listan och returnerar den summan.
Se till att ta hand om specialfallen när listans längd är 0 eller 1.
 
Körexempel:
>>> add_first_and_last([])
0
>>> add_first_and_last([2, 7, 4, 3])
5
>>> add_first_and_last([10])
10
"""


def add_first_and_last(num_list):
    if len(num_list) == 0:
        return 0
    if len(num_list) == 1:
        return num_list[0]
    return num_list[0] + num_list[len(num_list) - 1]


print(add_first_and_last([]))

print(add_first_and_last([2, 7, 4, 3]))

print(add_first_and_last([10]))