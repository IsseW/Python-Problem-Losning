"""
1. Bankomat
Låt användaren mata in ett uttagsbelopp, och beräkna hur många 100-lappar, 200-lappar och 500-
lappar bankomaten ska mata ut. Visa resultatet i terminalen.
"""


def split_money(amount):

    if amount % 100 != 0:
        return "Error"

    fivehundred = amount // 500
    amount -= fivehundred * 500
    twohundred = amount // 200
    amount -= twohundred * 200
    hundred = amount // 100
    amount -= hundred * 100

    return [fivehundred, twohundred, hundred]


withdrawal = int(input("Hur mycket pengar vill vill du ha: "))

cash = split_money(withdrawal)

print("500: " + str(cash[0]) + "\n200: " + str(cash[1]) + "\n100: " + str(cash[2]))