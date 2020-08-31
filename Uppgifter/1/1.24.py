"""
Övning 1.24 - Skottår
Enligt den Gregorianska kalendern så infaller skottår enligt följande regler: Året är ett skottår
om året är jämnt delbart på 4, men inte på 100. Om året är jämnt delbart på 100, måste året vara jämnt delbart på 400 om det ska vara ett skottår. Dvs år 1100, 1300, 1700 är inte skottår. Däremot är 400, 800, 1200, 1600, 2000 skottår.
Tips! Använd modulus-operatorn (%).
Uppgiften går ut på att skriva ett program som tar ett årtal (heltal) som användarinmatning,
därefter ska programmet skriva ut om det inmatade året är ett skottår eller inte.
"""


def is_leap_year(year: int):
    # Om året är delbart med 400 är det ett skottår
    # Om året är delbart med 4 men inte delbart med 100 är det också ett skottår
    return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)


print(str(is_leap_year(int(input("Year: ")))))