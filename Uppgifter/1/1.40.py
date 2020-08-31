"""
Övning 1.40 - Miniräknare
I denna uppgift ska du implementera en enkel miniräknare som klarar av operationerna +, −, ·, /.
Det vill säga det ska vara möjligt att addera, subtrahera, multiplicera och dividera två heltal
som användaren matar in. Användargränssnittet ska ha ett menysystem.
Menysystemet ska ha följande utseende :

1. Enter two integers
2. Add
3. Subtract
4. Multiply
5. Divide
0. Exit
Your choice: 
"""

a = 0
b = 0

while True:
    choice = int(
        input(
            "1. Enter two integers\n2. Add\n3. Subtract\n4. Multiply\n5. Divide\n0. Exit\nYour choice: "
        )
    )
    if choice == 0:
        break

    if choice == 1:
        a = int(input("A: "))
        b = int(input("B: "))
    elif choice == 2:
        print(a + b)
    elif choice == 3:
        print(a - b)
    elif choice == 4:
        print(a * b)
    elif choice == 5:
        if b != 0:
            print(a / b)
    else:
        print("Action " + str(choice) + " does not exist")