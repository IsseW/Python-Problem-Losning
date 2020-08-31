"""
Funktioner
Övning 1.8 - Plus
Skriv en funktion plus(x_value, y_value), som returnerar summan av de två talen som ges som parametrar.
"""


def plus(x_value, y_value):
    return x_value + y_value


print("X + Y = " + str(plus(int(input("X: ")), int(input("Y: ")))))