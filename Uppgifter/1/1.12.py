"""
Övning 1.12 - Body Mass Index (BMI)
Skriv en funktion som beräknar en persons BMI.

BMI = vikt(kg) / (längd(m) * längd(m))

>>> bmi(63, 1.70) 
'21.8'
>>> bmi(110, 2.00) 
'27.5'
"""


def bmi(mass, length):
    return mass / (length * length)


print(
    "Your BMI is "
    + str(
        bmi(float(input("Your mass in kg: ")), float(input("Your height in meters: ")))
    )
)
