"""
Övning 2.19 - Utvidga listelement
Skriv en funktion extend_each(my_item, my_list) som tar in ett värde och en lista av listor.
Funktionen ska utvidga varje sublista med det inskickade värdet som element. Skillnaden mellan den här funktionen och den förra är att orginallistan ska förändras.
Körexempel:
>>> old_list = [['kangar'], ['z'], ['f']]
>>> extend_each('oo', old_list)
>>> old_list
[['kangar', 'oo'], ['z', 'oo'], ['f', 'oo']]
"""


def extend_each(my_item, my_list):
    for i in range(len(my_list)):
        my_list[i].append(my_item)
    return my_list


old_list = [["kangar"], ["z"], ["f"]]
extend_each("oo", old_list)
print(old_list)