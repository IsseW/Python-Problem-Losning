"""
Övning 3.7 - Innehåll som inte är gemensamt
Skriv en funktion not_common(tup1, tup2) som tar in två tupler som argument och returnerar en tupel som innehåller alla element som inte är gemensamma för de två tuplerna. Resultat-tupeln ska vara sorterad. 

Körexempel
>>> not_common((1, 2, 3, 4), (3, 4, 5, 6))
(1, 2, 5, 6)

>>> not_common(('b', 'a', 'c', 'd'), ('a', 'b', 'c'))
('d',)

>>> not_common(('a', 'b', 'c'), ('a', 'b', 'c'))
()

>>> not_common(('a', 'b'), ('c', 'd'))
('a', 'b', 'c', 'd')

>>> not_common(('b', 'a', 'd', 'c'), ('a', 'b'))
('c', 'd')
"""


def not_common(tup1, tup2):
    list2 = list(tup2)

    l = []
    for t in tup1:
        if not t in tup2:
            l.append(t)
        else:
            list2.remove(t)
    l += list2
    return tuple(l)


print(not_common((1, 2, 3, 4), (3, 4, 5, 6)))
print(not_common(("b", "a", "c", "d"), ("a", "b", "c")))
print(not_common(("a", "b", "c"), ("a", "b", "c")))
print(not_common(("a", "b"), ("c", "d")))
print(not_common(("b", "a", "d", "c"), ("a", "b")))
