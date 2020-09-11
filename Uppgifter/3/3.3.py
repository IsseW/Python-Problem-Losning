"""
Övning 3.3 - Par utan ordning
Skriv en funktion unordered_pairs(my_list) som baserat på en lista genererar en lista av par (tupler),
som består av alla möjliga sätt att kombinera två element från original-listan då ordningen inte spelar roll, så paret  LaTeX: (x, y)( x , y ) räknas som samma par som LaTeX: (y, x)( y , x ). 
Körexempel:
 
>>> unordered_pairs([1, 2, 3])
[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
"""


def unordered_pairs(list):
    pair_list = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            pair_list.append((list[i], list[j]))
    return pair_list


print(unordered_pairs([1, 2, 3]))