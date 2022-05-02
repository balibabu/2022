'''variable with same value have id'''
a=5
b=5
print('id of a:',id(a))
print('id of b:',id(b))
del a
print('id of a:',id(a))


