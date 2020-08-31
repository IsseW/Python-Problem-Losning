"""
Övning 1.17 - Glass-maskinen
Skriv ett program som låter användaren mata in ett svar till frågan om man gillar glass eller inte. En körning av programmet kan se ut så här:

Do you like ice cream (yes/no)? yes
Yay! Me too.
Om användaren väljer att mata in no istället kan det se ut så här:

Do you like ice cream (yes/no)? no
Boo! :-(
Utvidga ditt program med enkel felhantering som tar hand om oriktiga inmatninger (dvs något annat än yes eller no).
I så fall ska programmet uppvisa följande beteende:

Do you like ice cream (yes/no)? maybe
Input error!
"""


def get_answer(text):
    answers = {"yes": "Yay! Me too.", "no": "Boo! :-("}
    return answers.get(text, "Input error!")


print(get_answer(input("Do you like ice cream (yes/no)? ")))