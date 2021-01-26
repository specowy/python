import random

name = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
name = [name[0] for name in name]
print('--List Comprehension 1--')
print(name)

lst = [[random.randrange(1, 10) for element in range(4)] for y in range(5)]
print('--List Comprehension 2--')
print(lst)
