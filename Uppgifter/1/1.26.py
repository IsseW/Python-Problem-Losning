"""
Övning 1.26 - Funktion med default-parametrar
Skriv en funktion som presenterar en person med namn och ålder och har default-parametrar.

>>> introduce("Linn", 19)
'My name is Linn. I am 19 years old.'
>>> introduce("Carina")
'My name is Carina. My age is a secret.'
>>> introduce()
'My name is unknown. My age is a secret.'
"""


def introduce(name="unknown", age=-1):
    print("My name is " + name, end=". ")
    if age < 0:
        print("My age is a secret.")
    else:
        print("I am " + str(age) + " years old.")


introduce("Isidor", 18)

introduce("Sexty")

introduce()