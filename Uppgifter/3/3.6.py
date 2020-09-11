"""
Övning 3.6 - Gemensamt innehåll
Skriv en funktion common_content(tup1, tup2) som tar in två tupler som argument och returnerar en tupel som innehåller alla element gemensamma 
för båda de inskickade.

Körexempel
>>> common_content((1, 2, 3), (2, 5, 1))
(1, 2)

>>> common_content((1, 2, 3, 'p', 'n'), (2, 5 , 1, 'p'))
    (1, 2, 'p')

>>> common_content((1, 3, 'p', 'n'), ('a', 2, 5, 1, 'p'))
    (1, 'p')
"""


def common_content(tup1, tup2):
    list = []
    for t in tup1:
        if t in tup2:
            list.append(t)

    return tuple(list)


print(common_content((1, 2, 3, "p", "n"), (2, 5, 1, "p")))
print(common_content((1, 3, "p", "n"), ("a", 2, 5, 1, "p")))
