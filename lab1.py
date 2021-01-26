import re

bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''

pattern_1 = re.compile("Niebieski", re.IGNORECASE)
result_1 = pattern_1.finditer(bridge_of_death)
print(type(result_1))

for substring in result_1:
    print(substring)
    print(substring.start())
    print(substring.span())
    print(substring.group())
