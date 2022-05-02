#tuple help
a=(1,2,3,[2,3])
print(a)
print(a*2)
print(a[1])
a[3].append(5) #but in case of list
#a[2] = 2   #single element in tuple is immutable
print(a)
#a.append(7)    #tuple itself is immutable
print(a)


#list help
list1=[1,4,2,6,8,3]
list1.sort(reverse=True)
list1.sort(key=value)
print(list1)
