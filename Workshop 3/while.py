"""
Uppgift 1 - while-loop
Skriv ett program, som frågar efter ett heltal mindre än 100. Programmet ska sedan summera detta tal och alla i ordningen efterföljande heltal tills 
summan av talen är större än tvåhundra. 
Skriv ut det sista talet som tas till summan och hela summan.
"""

should_exit = False
sum = 0
while (not should_exit) and sum < 200:
    input_string = input("Enter a number less than 100: ")
    if input_string == "q" or input_string == "quit":
        should_exit = True
    else:
        num = int(input_string)
        if num >= 100:
            print(num, "is not less than 100.")
        else:
            sum += num
            print("Sum = ", sum)