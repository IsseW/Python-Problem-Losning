"""
Övning 1.10 - Medelvärde
Skriv en funktion mean(x_value, y_value), som returnerar medelvärdet av de två talen som ges som parametrar.
"""


def mean(x_value, y_value):
    return (x_value + y_value) / 2


print("Medelvärdet av X och Y är " + str(mean(int(input("X: ")), int(input("Y: ")))))