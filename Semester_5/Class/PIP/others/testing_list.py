q=[1,2,'a','bali']
print(q)

list1=[[1,2,3],[4,5,6]]
print(len(list1))

print(q*2)
list2=[1,'a']
print(2*list2)
list3=[1,2]
print(2*list3)

print(list2+list3)
print(list3+list2)
print(list3+['a']) # we can only add list in list
print(list3+[['a']])
#print(list3+5)
#print(list3+'a')

print('max=',max(list3)) #list max help
print(max(['a','b','c']))
print(max(['ab','bz','cb','cz']))
print(max(['ab','bz','cb','cz','cz']))
#print(min(list2))
#print(max(list2)) list help: max or min only works for similar type of elements
#all elements should be either integers or chars or strings
l1=[[1,2,3],[2,2,1]]
print('max in l1',max(l1))

print(sum(list3))
#print(sum(list2))
#print(sum(['a','b'])) can't perform sum on chars list or mixture
list4=[1,2,3,4,5,6,7,8]
print(list4[3:6])

print(6  in list4)

print(list4.append(9)) #haha returns None
print(list4)
list4.append([10,11]) #adds as single element as whole
print(list4)
list4.extend([10,11]) #adds all elements
print(list4)

list4.reverse()
print(list4)
#list4.sort() #all elements should be of same type
list5=[5,7,6,1,2,3,4]
list5.sort(reverse=True) #for decending
print(list5)

del list5[1]
print(list5)
del list5[1:-1:2]
print(list5)

list6=[1,2,3,4,1,2,3,1]
list6.remove(1) #list remove help: removes only first occurence
print(list6)
