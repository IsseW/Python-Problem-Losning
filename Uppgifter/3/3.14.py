"""
Övning 3.14 - Mera gener
En DNA-sträng består av 4 nukleotidbaser och kan representeras av en sträng med bokstäverna:  A,T, C, G.  
Skriv en funktion som beräknar sammansättningen hos en sådan sträng. 
Funktionen ska returnera en dictionary med de fyra nycklarna 'A', 'T', 'C' och 'G' och antalet av respektive nukleotidbas som värden. 
Körexempel:
>>> base_composition("CTATCGGCACCCTTTCAGCA")
{'A': 4, 'C': 8, 'T': 5, 'G': 3}
    
>>> base_composition("AGT")
{'A': 1, 'C': 0, 'T': 1, 'G': 1}
"""


def base_composition(string):
    count_dic = {"A": 0, "T": 0, "C": 0, "G": 0}
    for c in string:
        if c in count_dic:
            count_dic[c] += 1
    return count_dic


print(base_composition("CTATCGGCACCCTTTCAGCA"))
print(base_composition("AGT"))