"""
Övning 1.37 - Multiplikationstabell
Skriv ett program som tar ett in ett tal som matas in av användaren.

Programmet ska skriva ut motsvarande multiplikationstabell i terminalen.
Du ska använda iteration för att lösa uppgiften!

En lyckad körning av programmet kan se ut så här:

This program prints out a multiplication table.
Enter a number: 7
0 * 7 = 0
1 * 7 = 7
2 * 7 = 14
3 * 7 = 21
4 * 7 = 28
5 * 7 = 35
6 * 7 = 42
7 * 7 = 49
8 * 7 = 56
9 * 7 = 63
"""
print("This program prints out a multiplication table.")
num = int(input("Enter a number: "))
for i in range(10):
    print(str(i) + " * " + str(num) + " = " + str(i * num))
