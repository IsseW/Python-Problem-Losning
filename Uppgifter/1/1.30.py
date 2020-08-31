"""
Iteration
Övning 1.30 - Utskrift med hjälp av loop
Skriv ett program som använder en for-loop för utskrift av

a) Alla heltalen mellan 0 och 25:  0, 1, 2, . . . , 23, 24, 25.

b) Alla heltalen mellan 0 och 25 fast baklänges:  25, 24, 23, . . . , 2, 1, 0.

c) Alla jämna tal mellan 0 och 30. (Tips! Kan göras med hjälp av %-operatorn.)

d) Summera alla heltal mellan 37 och 149, och presentera resultatet.

e) Summera alla heltal i ett intervall som användaren anger gränserna för. Skriv ut resultatet.
"""

print("a)", end=" ")
for i in range(26):
    print(i, end=", ")

print("")
print("")
print("b)", end=" ")
for i in range(25, 0, -1):
    print(i, end=", ")


print("")
print("")
print("c)", end=" ")
for i in range(0, 30, 2):
    print(i, end=", ")


print("")
print("")

sum = 0

for i in range(37, 149):
    sum += i
print("d) " + str(sum))

print("")
print("e)")

min = int(input("From: "))
max = int(input("To: "))


sum = 0
for i in range(min, max):
    sum += i
print("sum = " + str(sum))