"""
Övning 3.12 - Visa ordlista
Skriv en funktion show_wordlist(w_list) som går igenom en dictionary och skriver värdena för respektive nyckel. 
Om vi kör funktionen på numbers från en övning ovan borde det se ut så här. Kom ihåg att dictionaries inte har någon definierad ordning.
>>> show_wordlist(numbers)
--
one - 1
seven - 6
eight - 9
two - 2
-- 
"""


def show_wordlist(w_list):
    for t in w_list:
        print(t, " - ", w_list[t])


numbers = {"one": 1, "two": 2, "seven": 6, "eight": 9}
show_wordlist(numbers)