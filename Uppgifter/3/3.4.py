"""
Övning 3.4 - ☆Determinant för 2x2-matris
Determinant of a 2x2-matris är produkten av elementen i huvud-diagonalen minus produkten av de övriga elementen. Skriv en Python-funktion  det(matrix) som beräknar en sådan determinant.
Matrisen är representerad av en nästlad tupel där (en tupel där varje rad representeras som en tupel av värden).
 
Körexempel
>>> M = ((3, 1), (5, 2))
>>> det(M) 
1
"""

def det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

M = ((3, 1), (5, 2))

print(det(M))