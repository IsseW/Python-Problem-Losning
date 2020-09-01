"""
Övning 2.22 - ☆ Transponera en matris
Transponatet AT till en tvådimensionell matris A får man om man växlar matrisens rader och kolumner. 

Exempel med 3x2-matris 

LaTeX: A = 
 \begin{pmatrix}
  1 & 3  \\
  -5 & 6 \\
  2 & 4  
 \end{pmatrix}A = ( 1 3 − 5 6 2 4 )              LaTeX: A^{T}  = 
 \begin{pmatrix}
  1 & -5 & 3  \\
  3 & 6 & 4
 \end{pmatrix}A T = ( 1 − 5 3 3 6 4 )

Skriv en funktion transpose(matrix) som returnerar transponatet till en matris representerad som en nästlad lista.

Körexempel:

>>> A = [[1, 2, 3], [4, 5, 6]]
>>> transpose(A)
[[1, 4], [2, 5], [3, 6]]
>>> transpose([[1, 2]])
[[1], [2]]
>>> transpose([[3]])
[[3]]
"""


def transpose(matrix):
    new_matrix = []