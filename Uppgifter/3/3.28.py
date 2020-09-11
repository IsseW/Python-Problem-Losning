"""
Övning 3.28 - Ange alla tal mellan 
Skriv en rekursiv funktion numbers_between(start, end) som returnerar en komma-separerad sträng innehållande alla tal från och med  start till och med end.
Körexempel:

>>> numbers_between(2, 5)
'2,3,4,5'

>>> numbers_between(4, 4)
'4' 

>>> numbers_between(7, 11)
'7,8,9,10,11'
"""


def numbers_between(start, end, current=0):
    return (
        str(start + current) + ", " + numbers_between(start, end, current + 1)
        if start + current < end
        else str(end)
    )


print(numbers_between(2, 5))
print(numbers_between(4, 4))
print(numbers_between(7, 11))
