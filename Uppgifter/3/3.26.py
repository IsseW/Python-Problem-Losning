"""
Övning 3.26 - Infoga streck
Skriv en rekursiv funktion add_dashes(word) som tar in en sträng med ett ord och returnerar en ny sträng med alla tecken separerade med en  "-".
>>> add_dashes('duck')
'd-u-c-k'

>>> add_dashes('h')
'h'

>>> add_dashes('')
None
"""


def add_dashes(word, index=0):
    if len(word) == 0:
        return None
    if index == len(word) - 1:
        return word[index]
    return word[index] + "-" + add_dashes(word, index + 1)


print(add_dashes("duck"))
print(add_dashes("h"))
print(add_dashes(""))
