"""
Övning 2.3 - Räkna förekomst av ett tecken
Skriv en funktion, count_char(string, char), som räknar antalet förekomster av tecknet char i strängen string.

Körexempel:

>>> count_char(’elephant’, 'e')
2
>>> count_char(’Lion’, 'i')
1
>>> count_char(’Giraffe’, 'g')
0
"""


def count_char(word: str, char: str):
    count = 0
    for i in range(len(word)):
        if word[i] == char:
            count += 1
    return count


word = input("Write a word: ")

char = ""

# Få input tills det bara är en karaktär
while len(char) != 1:
    char = input("Write one character: ")


print(
    "In the word '"
    + word
    + "' there are "
    + str(count_char(word, char))
    + " occurrences of the letter '"
    + char
    + "'."
)