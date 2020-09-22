"""
Uppgift 2 - for-loop
Skriv ett program, som frågar efter ett heltaltal (startvärde) och ett annat tal som är större än startvärdet (sluttal). 
Programkoden ska summera samtliga tal från och med startvärdet till och med sluttalet med hjälp av en for-loop.
Skriv ut totalsumman.
"""

start_num = int(input("Start: "))
stop_num = int(input("Stop: "))

sum = 0
for i in range(start_num, stop_num + 1):
    sum += i

print("Sum = ", sum)