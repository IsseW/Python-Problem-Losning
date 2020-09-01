"""
Övning 2.5 - Hämta ett tecken
En sträng är som bekant en sekvens av tecken. Ett tecken i en sträng kan nås genom att använda index, där index för första positionen i strängen är 0.

Skriv en funktion get_char(string, position) som returnerar det tecken som finns på indexplats position  i string.

Om den angivna positionen i strängen inte existerar ska ett felmeddelande returneras.

Körexempel:

>>> word = "elephant"
>>> word[0]
’e’
>>> word[-1]
’t’
>>> get_char("apple", 2)
’p’
>>> get_char("giraffe", 0)
’g’
>>> get_char("giraffe", 10)
’Invalid position.’
"""


def get_char(string, position):
    if position < 0 or position >= len(string):
        return "Invalid Position"
    return string[position]


print(get_char(input("Word: "), int(input("Position: "))))