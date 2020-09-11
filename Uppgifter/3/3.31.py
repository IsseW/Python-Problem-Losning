"""
Övning 3.31 - ☆ 2-faktorisera
Skriv en rekursiv funktion two_factors(num) som tar in ett positivt heltal som argument och returnerar en sträng sammansatt av ett 
udda heltal multiplicerat med tvåor så att det beräknade värdet blir num. Strängen ska vara formaterad så att det står lika många tvåor 
på båda sidor om det udda talet. Om det aktuella antalet tvåor är udda ska det vara en tvåa mer framför än bakom det udda talet. 
Observera att det udda talet kan vara 1.
Körexempel:
>>> two_factors(1)
'1'

>>> two_factors(2)
'2 * 1'

>>>two_factors(10)
'2 * 5'

>>> two_factors(20)
'2 * 5 * 2'

>>> two_factors(30)
'2 * 15'

>>> two_factors(32)
'2 * 2 * 2 * 1 * 2 * 2'

>>> two_factors(80)
'2 * 2 * 5 * 2 * 2'
"""


def two_factors(num):
    if num % 4 == 0:
        return "2 * " + str(two_factors(num // 4)) + " * 2"
    if num % 2 == 0:
        return "2 * " + str(num // 2)
    return str(num)


print(two_factors(1))
print(two_factors(2))
print(two_factors(10))
print(two_factors(20))
print(two_factors(30))
print(two_factors(32))
print(two_factors(80))