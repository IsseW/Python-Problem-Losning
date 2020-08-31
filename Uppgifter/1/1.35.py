"""
Övning 1.35 - Delbarhet I
Skriv ett program som summerar alla positiva heltal under 2000 som är jämt delbara med 3.
Generalisera sedan ditt program så att användaren kan mata in de två ovanstående parametrarna.
"""

max = int(input("Max num: "))
divisor = int(input("Divisor: "))
sum = 0
for i in range(max):
    if i % divisor == 0:
        sum += i

print("sum = " + str(sum))
