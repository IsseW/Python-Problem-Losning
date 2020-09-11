"""
Övning 3.11 - Egenskaper hos dictionary
Här ser vi två förslag till hur man skapar en dictionary. Det ena fungerar men inte det andra. 
Försök förutsäga vilken av dem som fungerar. Kontrollera sedan vid Python-prompten om du hade rätt.
 
>>> coordinates_one = {(1, 0): 'x-axis', (0, 1): 'y-axis'}
>>> coordinates_two = {[1, 0]: 'x-axis', [0, 1]: 'y-axis'}
 
Försök också förklara varför det ena sättet fungerar, men inte det andra.
"""

coordinates_one = {(1, 0): "x-axis", (0, 1): "y-axis"}
# Error
coordinates_two = {[1, 0]: "x-axis", [0, 1]: "y-axis"}

"""
Dictionaries använder hashen av ett object för index. En lista är en typ man inte kan få en hash av.
Man hade kunnat skriva en hashing funktion för en lista och på så sätt använt den i en dictionary.
"""