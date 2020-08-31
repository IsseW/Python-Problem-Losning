"""
Övning 1.34 - Gissa talet II
Här ska du implementera ett spel likt spelet (se Övning Gissa Talet I).

Spelreglerna är:

Programmet slumpar ett tal mellan 1 och 100.
Spelaren gissar ett tal
Beroende på spelarens gissning, så svarar programmet med ett av tre möjliga val: (i)
Spelaren gissade för högt. (ii) Spelare gissade för lågt. (iii) Spelaren gissade rätt. Detta
fortgår tills dess att spelaren gissat rätt.
Programmet presenterar hur många gissningar som gick åt, därefter avslutas programmet.
Extrauppgift: Låt användaren få en fråga innan programmet avslutas om spelet ska spelas
igen Y(es)/N(o). Om användaren svarar Y, låt spelet börja om. För att få in den funktionaliteten
kan du behöva ytterligare en loop (ytterst) i programmet.
"""

import random

while True:

    num = random.randint(1, 100)

    while True:
        inp = input("Guess (or e to exit): ")
        if inp == "e":
            print("The correct number is " + str(num))
            break
        guess = int(inp)

        if guess == num:
            print("Correct!")
            break
        if guess < num:
            print("The number is larger")
        else:
            print("The number is smaller")

    if input("Want to play again? y(es)/n(o)  ") != "y":
        break
