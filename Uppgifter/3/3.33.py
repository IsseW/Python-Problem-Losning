"""
Övning 3.33 - ☆☆ Sifferkonvergens
Ta ett godtyckligt icke-negativt heltal a med ett godtyckligt antal siffror.
Låt x beteckna antal siffror i talet, y antal udda siffror i talet och z antalet jämna siffror i talet.
Låt f(a) vara en funktion sådan att den ger det tal som består av en konkatenering (sammansättning) 
av siffrorna xyz enligt beskrivningen ovan.
 
Om man anropar f för resultatet f(a) rekursivt dvs f(f(a)) tills det inte blir någon skillnad i resultatet kommer det att alltid  
konvergera till samma resultat så småningom, oavsett vilket tal a man stoppat in till att börja med. 
Vilket tal konvergerar funktionens resultat till?
 
Skriv en rekursiv funktion i Python, som returnerar det resultat som alla tal konvergerar till enligt ovanstående beskrivning.
"""


def f(a):
    num_even = 0
    num_odd = 0
    while a > 0:
        digit = a % 10
        if digit % 2 == 0:
            num_even += 1
        else:
            num_odd += 1
        a //= 10
    return int(str(num_even + num_odd) + str(num_odd) + str(num_even))


def converge(num, times=100):
    num = f(num)
    return num if times <= 0 else converge(num, times - 1)


print(converge(9001))
print(converge(1337))
print(converge(420))
print(converge(69))

# Konvergerar till 321