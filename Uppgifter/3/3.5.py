"""
Övning 3.5 - Samma innehåll
Skriv en funktion same_content(tup1, tup2) som tar in två tupler som argument och returnerar LaTeX: \texttt{True}True om båda tuplerna innehåller samma element och LaTeX: \texttt{False}False annars.

Körexempel
>>> same_content((1, 2), (1, 2))
True
    
>>> same_content((1, 2), (1, 2, 1))
False

>>> same_content((1, 2), (2, 1))
True
    
>>> same_content((1, 2), ())
False
"""


def same_content(tup1, tup2):
    if len(tup1) != len(tup2):
        return False
    for t in tup1:
        if not t in tup2:
            return False
    return True


print(same_content((1, 2), (1, 2)))
print(same_content((1, 2), (1, 2, 1)))
print(same_content((1, 2), (2, 1)))
print(same_content((1, 2), ()))