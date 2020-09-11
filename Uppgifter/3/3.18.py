"""
Övning 3.18 - ☆ Tillbaka till gles vektor
Se beskrivning av ovanstående övningsuppgift. Skriv en funktion som tar in en komprimerad 
beskrivning av en gles vektor i form av en dictionary och omvandlar den till en lista .
Körexempel:
>>> dict_to_list({0: 1, 3: 2, 7: 3, 12: 4})
[1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]

>>> dict_to_list({0: 1, 2: 1, 4: 2, 6: 1, 9: 1})
[1, 0, 1, 0, 2, 0, 1, 0, 0, 1]

>>> dict_to_list({})
[]
"""


def dict_to_list(dict):
    if len(dict) == 0:
        return []
    return list(
        map(
            lambda x: 0 if not x in dict else dict[x],
            list(x for x in range(max(dict) + 1)),
        )
    )


print(dict_to_list({0: 1, 3: 2, 7: 3, 12: 4}))
print(dict_to_list({0: 1, 2: 1, 4: 2, 6: 1, 9: 1}))
print(dict_to_list({}))