"""
Övning 2.11 - Lägg till och ta bort element i en lista
Starta med följande list-deklaration:

a_list = ['Hello', 0]

a) Använd list-metoden append(x) för att lägga till element i listan så att den ser ut som listan i körexemplet nedan:

>>> a_list[0]
’Hello’
>>> a_list[1:3]
[0, 20.0]
>>> a_list[3]
’World’
 
b) En lista kan modifieras, och element kan även tas bort ur en lista.
Använd list-metoden remove(x) för att ta bort element ur en lista.
Utgå ifrån list-deklarationen:

a_list = ['hello', 'I', 'love', 'Python', 'programming']

Ta sedan bort element så att den återstående listan blir:
['hello', 'Python', 'programming']
"""

# a

a_list = ["Hello", 0]

a_list.append(20.0)
a_list.append("World")

# b

a_list = ["hello", "I", "love", "Python", "programming"]

a_list.remove("I")
a_list.remove("love")