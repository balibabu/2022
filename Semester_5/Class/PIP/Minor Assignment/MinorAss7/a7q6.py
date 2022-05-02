'''Write a function that takes n as an input and creates a list of n lists such that ith list contains first five
multiples of i.'''

num=int(input('enter a number '))
list1=list()
for i in range(1,num+1):
    a=[i*j for j in range(1,6)]
    list1.append(a)

print(list1)