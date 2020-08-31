"""
Övning 1.9 - Minus
Skriv en funktion minus(x_value, y_value), som returnerar differensen mellan de två talen som ges som parametrar.
"""


def minus(x_value, y_value):
    return x_value - y_value


print("X - Y = " + str(minus(int(input("X: ")), int(input("Y: ")))))