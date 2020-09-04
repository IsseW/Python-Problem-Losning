"""
3. Andragradsekvation med två rötter
En andragradsekvation på formen
x2+px+q=0
kan lösas av den så kallade pq-formeln

Gör ett program som först låter användaren mata in p och sedan q. Sedan ska
programmet beräkna och skriva ut de två rötterna.
Ekvationen kan ha noll, en eller två rötter. Ditt program behöver bara klara fallet att
ekvationen har två rötter. Exempelvis ska p=10 och q=5 ge rötterna
-0.5278640450004204 och -9.47213595499958.
"""

import math


def solve_pq(p, q):
    a = -(p / 2)

    b = (p / 2) ** 2 - q

    if b >= 0:
        c = math.sqrt(b)
        return a + c, a - c
    return "Error", "Error"


p = float(input("P: "))
q = float(input("Q: "))

solution1, solution2 = solve_pq(p, q)

print("x1 = " + str(solution1) + ", x2 = " + str(solution2))