"""
Övning 3.1 - Tupler
Tupler fungerar på ett sätt som liknar listor, men med två viktiga skillnader. Den första skillnaden är att man använder vanliga parenterser istället för hakparenteser för att rama in dem. Den andra skillnaden kommer du att upptäcka i den här övningen. Tupler kan, precis som listor, innehålla vilken datatyp som helst. Låt oss skriva följande i Python-terminalen för att representera en punkt LaTeX: (x,y)( x , y ) i ett koordinatsystem:
>>> point = (5, 0)
 
Försök sedan att ändra y-koordinaten till 5 i tupeln genom att göra access till enbart den positionen,  point[1]. Är det möjligt?
"""

point = (5, 0)

# Error
point[1] = 5
