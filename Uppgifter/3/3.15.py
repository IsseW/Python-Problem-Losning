"""
Övning 3.15 - Omvänd uppslagning
Skriv en funktion reverse_lookup(dictionary, value) som tar in en dictionary och ett värde som  argument och returnerar en sorterad lista med alla 
nycklar som är associerade med det värdet. Funktionen ska returnera en tom lista om man inte får någon träff.
>>> reverse_lookup({'a':1, 'b':2, 'c':2}, 1)
['a']

>>> reverse_lookup({'a':1, 'b':2, 'c':2}, 2)
['b', 'c']
    
>>> reverse_lookup({'a':1, 'b':2, 'c':2}, 3)
[]
"""


def reverse_lookup(dictionary, value):
    l = []
    for k in dictionary:
        if dictionary[k] == value:
            l.append(k)
    return l


print(reverse_lookup({"a": 1, "b": 2, "c": 2}, 1))
print(reverse_lookup({"a": 1, "b": 2, "c": 2}, 2))
print(reverse_lookup({"a": 1, "b": 2, "c": 2}, 3))
