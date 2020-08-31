"""
Övning 1.18 - Udda eller jämnt
Skriv ett program som frågar användaren efter ett heltal och utvärderar om talet är udda eller jämnt.
Nedan visas två olika körningar av programmet:

Write a number: 5 
5 is Odd
Write a number:  80
80 is Even
Utvidga programmet:

Steg1: Testa även om talet är en multipel av 4, och skriv i så fall ut ett lämpligt meddelande.

Steg2: Fråga användaren efter två heltal: ett tal att kontrollera (vi kan kalla det number) och ett tal att dela med (vi kan kalla det divisor).
Om divisor delar number jämnt skriv ut ett lämpligt meddelande till användaren, om inte skriv ut ett annat lämpligt meddelande.
"""


def is_divisible_by(int_num, divisor):
    return int_num % divisor == 0


def is_even(int_num):
    return is_divisible_by(int_num, 2)


test_int = int(input("Write a number: "))

if is_even(test_int):
    print(str(test_int) + " is Even")
    if is_divisible_by(test_int, 4):
        print(str(test_int) + " is divisible by 4")
    else:
        print(str(test_int) + " is not divisible by 4")

else:
    print(str(test_int) + " is Odd")
    print(str(test_int) + " is not divisible by 4")

divisor = int(input("Write a divisor to test with: "))

if is_divisible_by(test_int, divisor):
    print(str(test_int) + " is divisible by " + str(divisor))
else:
    print(str(test_int) + " is not divisible by " + str(divisor))