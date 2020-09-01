"""
Övning 2.8 - Läsa en fil
Skriv ett program som läser innehållet från en text-fil till datorns minne i en sträng.
Skriv sedan ut strängen i terminalen för att visa att programmet fungerar som det ska.
"""
import os

filepath = input("Enter a file path: ")

if os.path.isfile(filepath):
    file = open(filepath, "r")
    print(file.read())
    file.close()
else:
    print("The file '" + filepath + "' does not exist!")