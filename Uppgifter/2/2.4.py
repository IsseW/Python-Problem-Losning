"""
Övning 2.4 - Hitta substräng
Skriv en funktion search(string, substring) som returnerar det index där första förekomsten av substring  i string börjar.

Om substring inte finns i string ska funktionen returnera -1.

Körexempel:

>>> search(’elephant’, ’ant’)
5
>>> search(’apple’, ’p’)
1
>>> search(’Giraffe’, ’Aff’)
-1
"""


def search(text: str, query: str):
    # loopa genom alla karaktärer i text
    for i in range(len(text)):
        # om längden av query ligger utanför text finns inte query i text
        if i + len(query) >= len(text):
            break

        found = True

        # Loopa igenom query på karaktären "i" i text
        for j in range(len(query)):
            # om likheten inte stämmer är query inte på denna positionen
            if text[i + j] != query[j]:
                found = False
                break
        # om vi har loopat igenom hela query utan att hitta en olikhet har vi hittat query i text,
        # då returnar vi "i"
        if found:
            return i
    return -1


word = input("Word: ")

query = input("Query: ")

pos = search(word, query)

if pos < 0:
    print("'" + query + "' doesn't exist in '" + word + "'")
else:
    print("'" + query + "' is on the " + str(pos) + "th position in '" + word + "'")
