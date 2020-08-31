"""
Övning 1.21 - Likbent triangel
Skriv en funktion is_isosceles(x, y, z)som tar in måtten av de tre sidorna i en triangel, och returnerar sanningsvärdet True om det är en likbent triangel, annat fall ska den returnera False.
En likbent triangel har två sidor som är lika stora. En liksidig triangel är ett specialfall av en likbent triangel.Tänk på att alla sidor i en triangel måste vara större än noll för att det ska bli en triangel.
När funktionen körs från Python-terminalen ska det se ut så här:

>>> is_isosceles(2, 4, 3)
False
>>> is_isosceles(3, 3, 3)
True
>>> is_isosceles(2, 4, 2)
True
>>> is_isosceles(-2, 4, -2)
False
>>> is_isosceles(0, 0, 2)
False
"""


def is_isosceles(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return False
    if x == y or x == z or y == z:
        return True
    return False


print(str(is_isosceles(int(input("X: ")), int(input("Y: ")), int(input("Z: ")))))