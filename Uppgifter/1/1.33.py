"""
Övning 1.33 - Ränta på ränta
När man sätter in pengar på banken får man ränta på insatt kapital, dvs. kapitalet som är
insatt i banken ökar med ett viss en procent varje år. Om man till exempel sätter in 10 000 kronor
med 4% ränta har man 10000 · 1.04 = 10400 kronor efter första året. Andra året har man
10400 · 1.04 = 10816 kronor, tredje året 10000 · 1.04 · 1.04 · 1.04 = 11248.64 osv
Skriv ett program som låter användaren ange startbelopp, räntesats i procent och antal år som kapitalet förräntar sig. Därefter ska ditt program använda en loop för att beräkna hur mycket pengar användaren har på sitt konto efter dessa år. Låt slutligen programmet presentera slutsumman genom skriva ut den på skärmen.

Extrauppgift: Istället för att använda en loop kan man använda följande matematiska formel
för att beräkna totalbeloppet:
totalbelopp = startbelopp · räntefaktor^antalÅr
"""

inc = 1 + float(input("Ränta i procent: ")) / 100
years = int(input("Antal år: "))
start = float(input("Start kapital: "))
money = start
for i in range(years):
    money *= inc

print(money)

# Extrauppgift
print("☆")

print(start * (inc ** years))