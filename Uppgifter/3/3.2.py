"""
Övning 3.2 - Bilda alla par
Skriv en funktion all_pairs(my_list) som baserat på en lista genererar en lista av par (tupler),
som består av alla möjliga sätt att kombinera två element från original-listan. Ordningen spelar roll, så paret  LaTeX: (x, y)( x , y ) räknas som ett annat par än LaTeX: (y, x)( y , x ). Det betyder att om längden på orginallistan är LaTeX: nn, så blir längden på den resulterande listan LaTeX: n^{2} n 2.
Körexempel:
 
>>> all_pairs([1, 2, 3])
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
"""


def all_pairs(list):
    pair_list = []
    for i in list:
        for j in list:
            pair_list.append((i, j))
    return pair_list


print(all_pairs([1, 2, 3]))