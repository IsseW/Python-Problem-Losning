"""
Övning 1.22 - Vem är äldst?
Skriv ett program som frågar användaren efter dennes namn och födelseår. Födelseåret får inte
vara större än 2018 och inte mindre än 1900. Därefter ska ditt program presentera både namn
och ålder.
Utöka ditt program:
a) Programmet ska fråga två användare efter deras namn och födelseår. Därefter ska ditt program
skriva ut åldrarna och namnen, samt vem som är äldst.
b) Presentera även vem som är yngst.
c) Hantera också fallet där bägge personer är lika gamla
"""


def handle_person():
    namn = input("Namn: ")
    f = int(input("Födelse år: "))
    print(namn + " föddes år " + str(f))
    return namn, f


namn1, f1 = handle_person()

namn2, f2 = handle_person()

if f1 < f2:
    print(namn1 + " är äldre än " + namn2)
elif f2 < f1:
    print(namn2 + " är äldre än " + namn1)
else:
    print(namn1 + " och " + namn2 + " är lika gamla")