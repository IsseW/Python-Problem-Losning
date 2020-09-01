"""
Övning 2.7 - Palindrom
Skriv ett program som undersöker huruvida ett inmatat ord är palindrom eller inte.
Programmet ska fråga efter ett nytt ord upprepade gånger tills användaren matar in quit.
Körexempel:

Write a word: carrot
carrot is not a palindrome

Write a word: Mom
Mom is not a palindrome

Write a word: racecar
racecar is a palindrome

Write a word: quit
Exiting ...
"""


def is_palindrome(word: str):
    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


while True:
    inp = input("Write a word: ")

    if inp == "quit":
        break
    elif is_palindrome(inp):
        print("'" + inp + "' is a palindrome")
    else:
        print("'" + inp + "' is not a palindrome")

print("Exiting...")