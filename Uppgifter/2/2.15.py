"""
Övning 2.15 - Finn bokstav
Skriv en funktion som hittar en bokstav find_letter(character, letter_list) i ett ord,
där ordet representeras som en lista av bokstäver (bokstäver, dvs. tecken, representeras av strängar i Python).
Funktionen ska returnera  LaTeX: True om bokstaven finns i listan och False annars.
Körexempel:
>>> find_letter('u', ['h', 'o', 'u', 's', 'e'])
True
>>> find_letter('b', ['c', 'a', 'r'])
False
"""


def find_letter(character, letter_list):
    return character in letter_list


print(find_letter("u", ["h", "o", "u", "s", "e"]))
print(find_letter("b", ["c", "a", "r"]))
