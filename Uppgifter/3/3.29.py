"""
Övning 3.29 - Stjärnor
Skriv en rekursiv funktion two_pow_stars(num) som tar in ett positivt heltal och returnerar en sträng 
innehållande lika många stjärnor som 2^num anger
Körexempel:
>>> two_pow_stars(0)
'*'

>>> two_pow_stars(1)
'**'

>>> two_pow_stars(2)
'****'

>>>two_pow_stars(3)
'********'
"""


def two_pow_stars(num):
    return "*" if num == 0 else two_pow_stars(num - 1) * 2


print(two_pow_stars(0))
print(two_pow_stars(1))
print(two_pow_stars(2))
print(two_pow_stars(3))