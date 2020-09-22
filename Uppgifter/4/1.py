
# från 2.16
"""
Övning 4.1 - Enhetstest
Ta några av de programfunktioner du skrivit tidigare och enhetstesta dem "automatiskt" genom att anropa dem i assert-satser i 
jämförelse med korrekt utdata enligt samma princip som ovanstående exempel.
"""

def sum_last_digits(int_list):
    sum = 0
    for i in int_list:
        sum += i % 10
    return sum

assert sum_last_digits([123, 321, 312]) == 6
assert sum_last_digits([]) == 0
assert sum_last_digits([455]) == 5