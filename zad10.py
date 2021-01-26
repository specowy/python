import re
tense = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore'
print(re.findall(r"\b\w{4,}\b", tense))
