"""
Uppgift 1 - while-loop
Skriv ett program, som frågar efter ett heltal mindre än 100. Programmet ska sedan summera detta tal och alla i ordningen efterföljande heltal tills 
summan av talen är större än tvåhundra. 
Skriv ut det sista talet som tas till summan och hela summan.
"""



num = int(input("Enter a number less than 100: ")) - 1
sum = 0
while sum < 200:
    num += 1
    sum += num
print("Sum = ", sum)
print("Last number = ", num)