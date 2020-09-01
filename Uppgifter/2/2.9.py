"""
Övning 2.9 - Skriva en fil
Skriv en funktion som skriver alla multiplikationstabellerna upp till ett visst heltal till en fil.
Funktionen ska ta filnamnet (en sträng) och heltalet som inparametrar.
"""


def write(filename, num):
    file = open(filename, "w")
    for i in range(10):
        file.write(str(num * (i + 1)) + ", ")
    file.close()


write("test-2.9.txt", 7)
