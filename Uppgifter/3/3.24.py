"""
Övning 3.24 - Summera siffror
Skriv en rekursiv funktion sum_digits(int_num) som tar in ett heltal och returnerar summan av siffrorna i talet.
Körexempel:
>>> sum_digits(1234)
10

>>> sum_digits(4321)
10

>>> sum_digits(111)
3

>>> sum_digits(0)
0
"""


def sum_digits(num):
    return 0 if num == 0 else num % 10 + sum_digits(num // 10)


print(sum_digits(4321))
print(sum_digits(4321))
print(sum_digits(111))
print(sum_digits(0))