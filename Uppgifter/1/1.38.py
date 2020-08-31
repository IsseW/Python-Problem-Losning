"""
Övning 1.38 - Primtal
Definiera en funktion is_prime(number) som tar in ett heltal number som argument och returnerar  sanningsvärdet True om  talet är ett primtal, annars returneras False.
Ett tal är ett primtal  om det är större än 1 och inte har några andra positiva delare än 1 och talet självt.
>>> is_prime(97)
True
>>> is_prime(1)
False
>>> is_prime(-2)
False
>>> is_prime(10)
False
"""
import math


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True


print(is_prime(int(input("Test if number is prime: "))))