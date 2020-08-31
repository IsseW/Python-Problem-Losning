"""
Övning 1.31 - Vilka tal skrivs ut?
För varje deluppgift, studera koden och svara på frågorna!

a) Vad skrivs ut?

for i in range(0, 100, 3):
print(i)

svar: alla tal mellan 0, 100 jämnt delbara med 3

b) Vad skrivs ut?

i = 0
while i < 100:
    print(i)
    i *= 3
 
svar: oändlig loop, för i *= 3 kommer alltid vara 0 om i är 0 från början

 c) Vad skrivs ut?

k = 0
while 2*k + 1 < 100:
    print(2*k + 1)
    k += 1

svar: alla ojämna tal mellan 0 och 100 

d) Studera koden nedan, hur många gånger körs loopen? 

number = -1
for i in range(number):
    print("Hello!")

svar: 0 ggr

e) Studera koden nedan, hur många gånger körs loopen? 

number = 4
i = 0
while i < number:
    print("Hello!")
    i += 1

svar: 4 ggr
"""