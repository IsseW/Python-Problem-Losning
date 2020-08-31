"""
Övning 1.36 - Delbarhet II
Skriv ett program som summerar alla positiva heltal under 2000 som är jämt delbara med 3 eller 7.
"""


sum = 0
for i in range(2000):
    if i % 3 == 0 or i % 7 == 0:
        sum += i

print("sum = " + str(sum))