"""
Övning 3.30 - Skapa mönster
Skriv en rekursiv funktion pattern(num) som tar in en ett positivt heltal och skapar och returnerar en sträng med ett mönster. 
Mönstret ska följa följande regler:
Mitt-tecknet i strängen ska alltid vara en stjärna ('*').
Om strängen har ett jämnt antal tecken ska det vara två stjärnor i mitten.
Om det finns tecken före mittstjärnor lägger man till "mindre än"- tecken.
Om det finns tecken efter mittstjärnor lägger man till "större än"-tecken.
Mönstret ska alltid vara symmetriskt.
Körexempel:

>>> pattern(1)
'*'

>>> pattern(2)
'**'

>>> pattern(3)
'<*>'

>>> pattern(4)
'<**>'

>>> pattern(5)
'<<*>>'
"""


def pattern(num):
    if num == 0:
        return ""
    if num == 1:
        return "*"
    if num == 2:
        return "**"
    return "<" + pattern(num - 2) + ">"


print(pattern(0))
print(pattern(1))
print(pattern(2))
print(pattern(3))
print(pattern(4))
print(pattern(5))
print(pattern(6))