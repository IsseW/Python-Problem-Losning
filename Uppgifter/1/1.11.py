"""
Övning 1.11 - Fahrenheit och Celcius
Skriv en funktion som konverterar en temperatur från  Celsius-skala till Fahrenheit-skala.

Konverteringen sker enligt följande:

Multiplicera med 9.
Dividera med 5.
Addera 32.
"""


def celsius_to_fahrenheit(celsius):
    return 9 * celsius / 5 + 32


c = int(input("Temperature celsius: "))

print(str(c) + "°C = " + str(celsius_to_fahrenheit(c)) + "°F")