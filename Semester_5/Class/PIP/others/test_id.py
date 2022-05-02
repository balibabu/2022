#for search: id list id integer id float id

list1=[1,2,3]
list2=[1,2,3]
print('id of list1=',id(list1)) #id help in list: though value is same id is different
print('id of list2=',id(list2))
list3=list1
print('id of list3=',id(list3))

aa=3
bb=3
print(id(aa))  #but in integers id is same along with the values
print(id(bb))

aaa=3.1
bbb=3.1
print(id(aaa))  #also in floats id is same along with the values
print(id(bbb))

aa='a'
bb='a'
print(id(aa))  #also in char id is same along with the values
print(id(bb))

aa='aba'
bb='aba'
print(id(aa))  #also in string id is same along with the values
print(id(bb))