"""
Övning 1.14 - Pythagoras sats
Pythagoras sats som gäller för rätvinkliga trianglar kan skrivas som a2 + b2 = c2, där a och b är sidorna vid den räta vinkeln och c är hypotenusan.
Skriv en funktion som beräknar hyptenusan givet sidorna a och b.

Tips! Du kan använda math.sqrt(num)för att beräkna kvadratroten av num.
"""

import math


def pythagoras(a, b):
    return math.sqrt(a * a + b * b)


print(
    "Hyptenusan av en triangel med sidorna A och B är "
    + str(pythagoras(float(input("A: ")), float(input("B: "))))
)
