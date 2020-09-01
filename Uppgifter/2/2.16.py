"""
Övning 2.16 - Summera sista siffran
Skriv en funktion sum_last_digits(int_list) som summerar entalssiffran från alla tal i en lista av heltal.
 
Körexempel:
>>> numbers = [123, 23, 541, 2, 1]
>>> sum_last_digits(numbers)
10
>>> sum_last_digits([1, 2, 10])
3
"""


def sum_last_digits(int_list):
    sum = 0
    for i in int_list:
        sum += i % 10
    return sum


numbers = [123, 23, 541, 2, 1]
print(sum_last_digits(numbers))

print(sum_last_digits([1, 2, 10]))
