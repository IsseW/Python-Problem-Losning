"""
Övning 2.12 - Iterera genom en lista
Skriv en funktion add_numbers_in_list(num_list) som adderar alla tal i en lista som enbart innehåller tal och returnerar summan. 
Använd konstruktionen LaTeX: \texttt{for num in numbers}for num in numbers.
Körexempel:
>>> add_numbers_in_list([])
0
>>> add_numbers_in_list([10, 20, 30])
60
>>> add_numbers_in_list([-10, -20, 30])
0
"""


def add_numbers_in_list(num_list):

    sum = 0
    for num in num_list:
        sum += num
    return sum


print(add_numbers_in_list([]))
print(add_numbers_in_list([10, 20, 30]))
print(add_numbers_in_list([-10, -20, 30]))