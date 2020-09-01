"""
Övning 2.2 Räkna förekomst av 'e'
Skriv en funktion, count_e(word), som räknar förekomster av bokstaven 'e' (lower case) i det ord som skickas in som parameter.

Körexempel:

>>> count_e(’elephant’)
2
>>> count_e(’Egg’)
0
>>> count_e(’interference’)
4
"""


def count_e(word: str):
    count = 0
    for i in range(len(word)):
        if word[i] == "e":
            count += 1
    return count


word = input("Write a word: ")

print(
    "In the word '"
    + word
    + "' there are "
    + str(count_e(word))
    + " occurrences of the letter 'e'"
)
