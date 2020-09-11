"""
Övning 3.21 - Fibonacci
Fibonacci-talen är följande sekvens av heltal:  0, 1, 1, 2, 3, 5, 8, 13, 21, ..., 
där varje nytt tal formas genom att addera de två föregående. Sekvensen kan definieras rekursivt enligt följande:

Körexempel:

>>> fibonacci(1)
1 

>>> fibonacci(2)
1 

>>> fibonacci(3)
2

>>> fibonacci(4)
3 

>>> fibonacci(5)
5

>>> fibonacci(6)
8

>>> fibonacci(7)
13
"""


def fibonacci(num):
    return 1 if num == 1 or num == 0 else fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))