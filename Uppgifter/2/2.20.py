"""
Övning 2.20 - Caesarchiffer
Du ska implementera ett rotationschiffer som ibland kallas för Caesarchiffer.
Krypteringsmetoden går ut på att man förskjuter alla bokstäver med ett bestämt antal steg (med hjälp av en nyckel).
Om nyckeln exempelvis är 3 så förskjuts alla bokstäver i klartexten med 3 steg, dvs. alla 'A' blir 'D', alla 'Z' blir 'C'.

Tips: Det kan vara bra att göra en lista med alla alfabetets tecken i rätt ordning.

Du ska skriva två funktioner, en för kryptering och en för dekryptering:

encrypt(msg, key), som ska returnera den krypterade texten till klartexten msg.
decrypt(msg, key), som ska returnera den dekrypterade texten till kodtexten msg.
Din implementation ska följa nedanstående regler:

Endast de engelska bokstäverna ska krypteras (A-Z).
Gör ingen skillnad på små och stora bokstäver i krypteringsförfarandet,
dvs alla bokstäver kan göras om till versaler (upper case) innan krypteringen äger rum.
Tecken som inte är engelska bokstäver (punkter, mellanslag , ÅÄÖ, etc.) ska inte krypteras, utan bevaras oförändrade i texten.
>>> msg = 'Vi anfaller tidigt imorgon!'
>>> encrypt(msg, 5)
'AN FSKFQQJW YNINLY NRTWLTS!'
>>> msg = 'Bruce Wayne ̈ar Batman!'
>>> code = encrypt(msg, 17)
>>> code
'SILTV NRPEV ̈ÄI SRKDRE!'
>>> decrypt(code, 17)
'BRUCE WAYNE ̈ÄR BATMAN!'
"""


def try_get_char_code(character):
    code = ord(character)
    if code >= 65 and code <= 90:
        return True, code - 65
    if code >= 97 and code <= 122:
        return True, code - 97
    return False, -1


def get_letter(code):
    return chr(code + 65)


def clamp(code):
    c = code % 26
    if c < 0:
        c += 26
    return c


def encrypt(msg, key):
    new_msg = ""
    for c in msg:
        is_letter, letter_code = try_get_char_code(c)
        if is_letter:
            letter_code = clamp(letter_code + key)
            new_msg += get_letter(letter_code)
        else:
            new_msg += c
    return new_msg


def decrypt(msg, key):
    new_msg = ""
    for c in msg:
        is_letter, letter_code = try_get_char_code(c)
        if is_letter:
            letter_code = clamp(letter_code - key)
            new_msg += get_letter(letter_code)
        else:
            new_msg += c
    return new_msg


def int_input(str):
    while True:
        try:
            return int(input(str))
        except:
            print("Invalid input!")


while (
    inp := input(
        "What do you want to do?\n Encrypt(1), Decrypt(2) or 'q' to quit\nInput: "
    )
) != "q":
    if inp == "1":
        msg = input("Write a message to encrypt: ")
        key = int_input("Enter key: ")

        print("Encrypted msg: " + encrypt(msg, key))
    elif inp == "2":
        msg = input("Write a message to decrypt: ")
        key = int_input("Enter key: ")

        print("Decrypted msg: " + decrypt(msg, key))
    else:
        print("Invalid input!")
    print("")
