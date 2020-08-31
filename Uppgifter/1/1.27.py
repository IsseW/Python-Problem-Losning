"""
Övning 1.27 - Korrekta if-satser
Är det någon skillnad i hur de båda if-satserna nedan fungerar?
Vad är det i så fall för skillnad mellan dem?
För vilka värden på n ger de olika utskrifter?

if n < 0:
    print('Negative')
elif n < 1000:
    print('Small')
elif n > 1000:
    print('Large')
else:
    print('Medium')

if n > 1000:
    print('Large')
elif n < 1000:
    print('Small')
elif n < 0:
    print('Negative')
else:
    print('Medium')
"""

# I de andra if satserna kommer n < 0 aldrig nås eftersom allting som är mindre än 0 är också mindre än 1000.
# Det betyder att på negativa värden kommer första skriva 'Negative' medans den andra kommer skriva 'Small'

n = int(input("Write a number to test: "))

if n < 0:
    print("Negative")
elif n < 1000:
    print("Small")
elif n > 1000:
    print("Large")
else:
    print("Medium")

if n > 1000:
    print("Large")
elif n < 1000:
    print("Small")
elif n < 0:
    print("Negative")
else:
    print("Medium")
