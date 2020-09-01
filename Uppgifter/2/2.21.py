"""
Övning 2.21 - ☆ Matrisdimensioner
En tvådimensionell matris med dimensionerna mxn kan representeras i Python av en nästlad lista.

Exempel med 3x2-matris (3 rader med 2 tal i varje rad, dvs 2 kolumner):

Skriv en funktion matrix_dimensions(matrix)som returnerar dimensionerna för en 2d-matris som skickas in i form av en nästlad lista.
Funktionen ska returnera en informationssträng (se körexemplet nedan)

Körexempel:

>>> A = [ [1, 3], [-5, 6], [2, 4]]
>>> matrix_dimensions(A)
'This is a 3x2 matrix.'
>>> B = [ [1, 3, 2], [-5, 6, 0] ]
>>> matrix_dimensions(B)
'This is a 2x3 matrix.'
>>> C = [ [1, 3], [-5, 6, 0] ]
>>> matrix_dimensions(C)
'This is not a valid matrix.'
"""


def matrix_dimensions(matrix):
    width = len(matrix)
    if width == 0:
        return "This is a 0x0 matrix"
    height = len(matrix[0])
    for i in range(1, width):
        if len(matrix[i]) != height:
            return "This is not a valid matrix."
    return "This is a " + str(width) + "x" + str(height) + " matrix."


A = [[1, 3], [-5, 6], [2, 4]]
print(matrix_dimensions(A))

B = [[1, 3, 2], [-5, 6, 0]]
print(matrix_dimensions(B))

C = [[1, 3], [-5, 6, 0]]
print(matrix_dimensions(C))