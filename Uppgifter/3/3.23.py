"""
Övning 3.23 - Palindrom
En palindrom är ett ord, en fras, ett tal eller någoin annan sekvens som kan läsas med samma resultat både framifrån och bakifrån. Skriv en rekursiv funktion som tar reda på om ett givet ord är en palindrom eller inte.
Körexempel:
>>> is_palindrome("Racecar")
True

>>> is_palindrome("Never")
False

>>> is_palindrome("level")
True
 
Tips! 
Kontrollera först om första och sista bokstaven är lika.
Upprepa steg 1 rekursivt på substrängarna (med första och sista bokstaven borttagen).
"""


def is_palindrome(word, s=0, e=-1):
    return (
        True
        if s >= len(word) + e
        else word[s].upper() == word[e].upper() and is_palindrome(word, s + 1, e - 1)
    )


print(is_palindrome("Racecar"))
print(is_palindrome("Never"))
print(is_palindrome("level"))