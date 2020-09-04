"""
2. Medelvärde
Skriv ett program som låter användaren mata in två tal, och som beräknar och skriver ut medelvärdet
av dem.
Exempel:
Tal 1: -2.3
Tal 2: 3.6
Medelvärdet är 0.6500000000000001
"""


def mean(a, b):
    c = (a + b) / 2
    return c


a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

c = mean(a, b)

print("Medelvärdet är " + str(c))