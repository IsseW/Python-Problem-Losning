"""
Uppgift 3 - FizzBuzz
a) Skriv ett program som skiver ut talen 1 till 100 ett i taget.

b) Förändra programmet så att det skriver ut Fizz istället för talet om talet är jämt delbart med 3.

c) Förändra programmet så att det även skriver ut Buzz istället för talet om talet är jämt delbart med 5, 
och FizzBuzz istället för talet om talet är jämnt delbart med både 3 och 5.
"""

for i in range(1, 101):
    to_print = ""
    if i % 3 == 0:
        to_print += "Fizz"
    if i % 5 == 0:
        to_print += "Buzz"
    if len(to_print) == 0:
        to_print = str(i)
    print(to_print)