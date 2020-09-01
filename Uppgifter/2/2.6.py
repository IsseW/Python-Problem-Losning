"""
Övning 2.6 - Räkna vokaler
Skriv en funktion count_vowels(string)som räknar hur många vokaler som finns i strängen och returnerar detta antal. Det räcker om du undersöker vokalerna i det engelska alfabetet:  ’a’, ’e’, ’i’, ’o’, ’u’.
Körexempel:

>>> count_vowels('elephant')
3
>>> count_vowels('apple')
2
"""


def count_vowels(text: str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in range(len(text)):
        if text[i] in vowels:
            count += 1
    return count


print(str(count_vowels(input("Enter text: "))))