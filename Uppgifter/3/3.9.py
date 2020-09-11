"""
Övning 3.9 - Sortera med avseende på längd
Skriv en funktion sort_by_len(tup_list, direction) som tar in en tupel av strängar. 
Returnera en ny tupel där strängarna är sorterade med avseende på längd. Sorteringsordningen bestäms av andra argumentet som är en sträng  med innehållet 'asc' för stigande ordning och 'des' för fallande ordning.

Körexempel
>>> sort_by_len(('Windows', 'Linux', 'OSX'), 'asc')
('OSX', 'Linux', 'Windows')

>>> sort_by_len(('apple', 'orange', 'pear'), 'des')
('orange', 'apple', 'pear')

>>> sort_by_len(('begin', 'python', 'programming'), 'des')
('programming', 'python', 'begin')

>>> sort_by_len(('begin', 'python', 'programming'), 'asc')
('begin', 'python', 'programming')
"""


def sort_by_len(tup_list, direction):
    return tuple(
        sorted(
            tup_list,
            key=lambda a: len(a),
            reverse=False if direction == "asc" else True,
        )
    )


print(sort_by_len(("Windows", "Linux", "OSX"), "asc"))
print(sort_by_len(("apple", "orange", "pear"), "des"))
print(sort_by_len(("begin", "python", "programming"), "des"))
print(sort_by_len(("begin", "python", "programming"), "asc"))
