"""
Övning 3.25 - Räkna stora 'X'
Skriv en rekursiv funktion count_X(string) som tar in en sträng och returnerar antalet förekomster av det versala tecknet 'X' i strängen.
Körexempel:

>>> count_X('XERXES is an example')
2

>>> count_X('Xilinx')
1

>>> count_X('axe')
0
"""


def count_X(word, index=0):
    return (
        0
        if index >= len(word)
        else (1 if word[index] == "X" else 0) + count_X(word, index + 1)
    )


print(count_X("XERXES is an example"))
print(count_X("Xilinx"))
print(count_X("axe"))
