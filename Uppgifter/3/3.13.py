"""
Övning 3.13 - Gener
Transkription, eller RNA-syntes, är den process varmed genetisk information i cellens DNA översätts till information i RNA. 
Vid transkriptionen byggs mRNA (budbärar-RNA) upp med DNA som mall. De 4 
nukleotidbaserna A, T, C, G korresponderar till mRNA-baserna U, A, G, C.
Skriv en funktion mRNA_transcript(template) som returnerar mRNA-transkriptet av en DNA-sträng.
Körexempel:
>>> mRNA_transcript("ATCGATTG")
'UAGCUAAC' 
 
Tips! Använd en dictionary för att mappa mellan DNA- och RNA-baser.
"""


def mRNA_transcript(template):
    COR = {"A": "U", "T": "A", "C": "G", "G": "C"}
    return "".join(map(lambda a: COR[a], template))


print(mRNA_transcript("ATCGATTG"))