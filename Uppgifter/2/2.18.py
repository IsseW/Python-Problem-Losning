"""
Övning 2.18 - Duplicera lista och distribuera värde till sublistor
Utforma en funktion distribute(my_item, my_list)som tar in ett värde och en lista av listor. Funktionen ska returnera en ny lista utgående från den medskickade listan, där värdet  my_item fogats in som element i varje sublista.

Körexempel:
>>> old_list = [['kangar'], ['z'], ['f']]
>>> distribute('oo', old_list)
[['kangar', 'oo'], ['z', 'oo'], ['f', 'oo']]
>>> old_list
[['kangar'], ['z'], ['f']]
"""


def distribute(my_item, my_list):
    new_list = []
    for l in my_list:
        new_list.append([])
        for i in l:
            new_list[len(new_list) - 1].append(i)
        new_list[len(new_list) - 1].append(my_item)
    return new_list


old_list = [["kangar"], ["z"], ["f"]]

print(distribute("oo", old_list))

print(old_list)