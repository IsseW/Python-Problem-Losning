"""
Övning 1.42 - ☆☆ Ramanujans formel för π
Skriv en funktion estimate_pi() för att beräkna och returnera ett närmevärde till π
baserat på den formel som hittades 1910  av den indiske matematikern Srinivasa Ramanujan. Denna formel konvergerar mot π mycket snabbare än Leibnitz formel. Använd en while-loop för att beräkna summationstermer tills den sista termen är mindre än LaTeX: 10^{-15}10 − 15.
Formeln ges nedan:
"""
import math


def factorial(number: int):
    if number == 0:
        return 1

    return number * factorial(number - 1)


def estimate_pi(k=100):
    sum = 0
    for i in range(k):
        sum += (
            factorial(4 * i)
            * (1103 + 26390 * i)
            / ((factorial(i) ** 4) * (396 ** (4 * i)))
        )
    return 1 / (sum * 2 * math.sqrt(2) / 9801)


print("π ≈ " + str(estimate_pi(int(input("k = ")))))