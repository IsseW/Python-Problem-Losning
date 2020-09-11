"""
Övningsuppgift 3.16 - Inverterad dictionary
Skriv en funktion invert_dictionary(my_dict) som tar en dictionary som argument och som inverterar returnerar en ny dictionary 
med nycklar och värden omvänt mot orginalet.

Körexempel
>>> invert_dictionary({'a':1, 'b':2, 'c':3, 'd':2})
{1: ['a'], 2: ['b', 'd'], 3: ['c']}

>>> invert_dictionary({'a':3, 'b':3, 'c':3})
{3: ['a', 'c', 'b']}
    
>>> invert_dictionary({'a':2, 'b':1, 'c':2, 'd':1})
{1: ['b', 'd'], 2: ['a', 'c']}
"""


def invert_dictionary(my_dict):
    new_dict = {}
    for k in my_dict:
        value = my_dict[k]
        if value in new_dict:
            new_dict[value].append(k)
        else:
            new_dict[value] = [k]
    return new_dict


print(invert_dictionary({"a": 1, "b": 2, "c": 3, "d": 2}))
print(invert_dictionary({"a": 3, "b": 3, "c": 3}))
print(invert_dictionary({"a": 2, "b": 1, "c": 2, "d": 1}))
