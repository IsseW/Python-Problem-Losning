"""
Övning 1.25 - Kasta tärning
Skriv ett tävlingsspel som går ut på att två spelare kastar varsin 6-sidig tärning därefter skriver
programmet ut den som vann, dvs den som fick högst tärningskast.
En körning av programmet kan se ut på följande sätt:

Player 1, enter your name: Christian
Player 2, enter your name: Cuong
Christian, your dice shows 4
Cuong, your dice shows 5
Winner is Cuong!
"""

import random

name1 = input("Player 1, enter your name: ")
name2 = input("Player 2, enter your name: ")

# random.randint(x, y) is inclusive
r1 = random.randint(1, 6)
r2 = random.randint(1, 6)

print(name1 + ", your dice shows " + str(r1))
print(name2 + ", your dice shows " + str(r2))

if r1 > r2:
    print("The winner is " + name1 + "!")
elif r2 > r1:
    print("The winner is " + name2 + "!")
else:
    print("It's a tie!")
