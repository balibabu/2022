#set in python
s={1,2}
print(s)
s.add('4')
s.add((8,9))
#s.add({1,2})
s.update('5')
s.update([3,4])
s.update({6,7})
s.update((11,12))
#s.add([9])
print(s)
print(s.pop()) #minimum ascii removed
print(s)
print(s.pop())
s.add(4)
print(s)
print(s.pop())

s.clear()
print(s)
