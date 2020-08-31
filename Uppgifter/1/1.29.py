"""
Övning 1.29 - ☆ Skriv om större if-sats
Skriv om nedanstående if-sats utan att använda nästling.
Den här komplicerade if-satsen kan faktiskt förenklas till bara 6 rader kod.

if n > 10:
    if n > 100:
        if n < 1000:
            print(n)
        else:
            if n < 1001:
                print('Pretty large')
            else:
                print(n)
    else:
        if n == 11:
            print(n)
        else:
            if n == 10:
                print('10!')
            else:
                print(n) 
else:
    if n < 0:
        print('Below zero')
    else:
        print(n)) 
"""

# Svaret till denna uppgiften fanns på canvas men var fel, de hade inte kollat då
# n == 10 och '10!' skulle printas.

n = int(input("Write a number: "))

if n < 0:
    print("Below zero")
elif n == 10:
    print("10!")
elif n == 1000:
    print("Pretty large")
else:
    print(n)