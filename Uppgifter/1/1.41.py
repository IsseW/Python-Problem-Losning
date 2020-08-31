"""
Övning 1.41 - ☆☆ Leibnitz formel för π
Det går att visa att följande oändliga summation:


går mot π (dock konvergerar serien långsamt).
Uppgiften går ut på att göra en implementation om beräknar seriens summa (med hjälp av iteration) för att beräkna närmevärden till π. Eftersom det är en oändlig serie, dvs. oändligt antal termer så är det inte rimligt att låta datorn iterera i all oändlighet. Därmed  krävs det en modifiering av formeln (en approximation):

Genom att öka värdet på k t.ex 100, 200, 300, . . . får du mer och mer noggranna närmevärden. Öka k i ditt program till dess att du börjar känna igen värdet på π.
Tips: Tänk på att (−1)n = 1 då n är jämnt och (−1)n = −1 då n är udda om du sätter ett tröskelvärde på storleken av termerna för att avbryta iterationen.


Anmärkning: Datorn arbetar med flyttal som är en approximation av ett decimaltal vilket leder till att beräkningar inte är exakta.
"""


def estimate_pi(k=100):
    sum = 0
    for i in range(k + 1):
        val = 1 / (2 * i + 1)
        if i % 2 == 0:
            sum += val
        else:
            sum -= val
    return 4 * sum


print("π ≈ " + str(estimate_pi(int(input("k = ")))))