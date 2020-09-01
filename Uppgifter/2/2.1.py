"""
Strängar och filer
Övning 2.1 - Omvandling med hjälp av ASCII-kod
Skriv en egen funktion som omvandlar en liten bokstav till en stor. Funktionen ska ta in en sträng med ett tecken och returnera en sträng med ett tecken. Om strängen innehåller ett annat tecken än en liten bokstav returneras det tecken som skickades in. 

De inbyggda Python-funktionerna ord(char) och chr(num)får användas.

Tips! Inspektera ASCII-tabellen.
"""


def to_upper(character):
    num = ord(character)
    # Kollar om det inte är en liten bokstav och isåfall bara returna input
    if num < 98 or num > 122:
        return character
    return chr(num - 32)


inp = ""

# Få input tills det bara är en karaktär
while len(inp) != 1:
    inp = input("Write one character: ")

print("To upper of '" + inp + "' is '" + to_upper(inp) + "'")