"""
Övning 1.39 - ☆ Fibonacci-tal
Ett Fibonaccital är ett tal som har följande egenskap:
 LaTeX: F(n) = \left\{
        \begin{array}{ll}
            0 & \text{om $n = 0$}\\
            1 & \text{om $n = 1$}\\
            F(n-1) + F(n-2) & \text{annars}.
        \end{array} \right.F ( n ) = { 0 om  n = 0 1 om  n = 1 F ( n − 1 ) + F ( n − 2 ) annars .

Det vill säga ett tal i följden är summan av de två föregående talen, förutom de två första talen
som är 0 respektive 1. Följden blir då:
 0, 1, 1, 2, 3, 5, 8, 13, 21, . . .
a) Du ska skriva ett program som låter användaren mata in n och presenterar F(n) (dvs. det n:te talet i följden).
b) Skriv om programmet så att den skriver ut hela följden F(0), F(1), F(2), F(3), . . . , F(n −1), F(n).
"""

n = int(input("Enter a number: "))

print("a)", end=" ")

a = 0
b = 1
c = 0

for i in range(n):
    c = b
    b += a
    a = c
print(b)

print("b)", end=" ")

a = 0
b = 1
c = 0

for i in range(n):
    c = b
    b += a
    a = c
    print(b, end=", ")