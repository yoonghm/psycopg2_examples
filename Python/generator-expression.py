#!/usr/bin/env python3

#line = input()
line = "trainer:housey;course:csharp-oop-basics;lecture:polymorphism;duration:3h05m"

tokens = ((kvp.split(':') for kvp in line.split(';')))

print(tokens)
'''
tokens is a generator expression. 
It could be converted to list, tuple or dictionary ONCE
'''

print(list(tokens))
'''
[['trainer', 'housey'], ['course', 'csharp-oop-basics'], ['lecture', 'polymorphism'], ['duration', '3h05m']]
'''

print(tuple(tokens))
'''
()
'''

print(dict(tokens))
'''
{}
'''

'''
We can convert generator expression at once
'''
print('-'*72)
print(list(((kvp.split(':') for kvp in line.split(';')))))
print('-'*72)
print(tuple(((kvp.split(':') for kvp in line.split(';')))))
print('-'*72)
print(dict(((kvp.split(':') for kvp in line.split(';')))))
