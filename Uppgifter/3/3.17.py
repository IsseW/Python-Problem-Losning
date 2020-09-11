"""
Övningsuppgift 3.17 - ☆ Gles vektor
En vektor är en matematisk konstruktion som består av en följd av tal av en viss längd. Vid datalagring används ofta vektorer 
för att lagra data, där positionen i vektorn för varje datadel är viktig för betydelsen. 
Många gånger består sådana datalagringsvektorer mest av nollor (tomrum), 
vilket är ett oekonomiskt sätt att lagra data då de mer eller mindre betydelselösa nollorna tar mycket plats.
 
Hos oss är vektorerna representerade som listor. Skriv en konverteringsfunktion som omvandlar en sådan lista till en dictionary, 
där endast de nollskilda värdena sparas med positionen (indexvärdet) som nyckel tillsammans med sitt värde.  
Körexempel:
>>> list_to_dict([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4])
{0: 1, 3: 2, 7: 3, 12: 4}
    
>>> list_to_dict([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0])
{0: 1, 2: 1, 4: 2, 6: 1, 9: 1}
    
>>> list_to_dict([0, 0, 0, 0, 0])
{}
"""


def list_to_dict(vector):
    sparse_vector = {}
    for i in range(len(vector)):
        if vector[i] != 0:
            sparse_vector[i] = vector[i]
    return sparse_vector


print(list_to_dict([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]))
print(list_to_dict([1, 0, 1, 0, 2, 0, 1, 0, 0, 1, 0]))
print(list_to_dict([0, 0, 0, 0, 0]))