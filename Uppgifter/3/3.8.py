"""
Övning 3.8 - Sortera med avseende på nummer
Skriv en funktion sort_by_number(tup_list) som tar in en lista av tupler med två element, där första elementet i tuplerna är ett tal.
Returnera en tupel sammansatt av andra elementet från var och en av tuplerna i den ursprungliga listan sorterade efter numret i samma ursprungstupel.

Körexempel
>>> sort_by_number([(6, 'DV1574'), (4, 'Python'), (5, 'course'), (1, 'Welcome'), (3, 'the'), (2, 'to')])
('Welcome', 'to', 'the', 'Python', 'course', 'DV1574')

>>> sort_by_number([(2, 'programming'), (3, 'is'), (1, 'Python'), (4, 'fun')])
('Python', 'programming', 'is', 'fun')

>>> sort_by_number([(2, 'are'), (3, 'Immutable'), (1, 'Tuples')])
('Tuples', 'are', 'Immutable')
"""


def sort_by_number(tup_list):
    return tuple(i[1] for i in sorted(tup_list, key=lambda a: a[0]))


print(
    sort_by_number(
        [
            (6, "DV1574"),
            (4, "Python"),
            (5, "course"),
            (1, "Welcome"),
            (3, "the"),
            (2, "to"),
        ]
    )
)
print(sort_by_number([(2, "programming"), (3, "is"), (1, "Python"), (4, "fun")]))
print(sort_by_number([(2, "are"), (3, "Immutable"), (1, "Tuples")]))
