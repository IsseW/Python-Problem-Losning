"""
Jobba med resterande tillsammans (programmera och diskutera) så långt ni hinner:
• Skriv en funktion som skriver Hello i terminalen.
• Skriv en funktion som tar in en parameter, radien, och beräknar och skriver ut arean på en
cirkel med den radien i terminalen.
• Skriv en funktion som tar in en parameter, radien, räknar ut arean på en cirkel med den
radien och returnerar värdet
"""

def area(radie):
    return (radie ** 2) * 3.141592



print("Hello")

radie = float(input("Enter a radius: "))

print(str(area(radie)))