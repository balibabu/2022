import re

string1 = 'Python Programming Language'
match1 = re.search('^P.*e$', string1)
print(match1.group())

match1 = re.search('[a-b]', string1)
print(match1.group())

n=12
for i in n:
    print(i)
