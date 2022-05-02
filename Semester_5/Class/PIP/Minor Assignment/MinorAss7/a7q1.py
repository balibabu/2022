# Write a function that takes a list of values as input parameter and returns another list without any
# duplicates.
def isPresent(list,value):
    for i in list:
        if value==i: return True
    return False

print('enter int values in list')
list1=list()
list2=list()
for i in range(5):
    list1.append(int(input()))

print('list without element repeatition')
for i in list1:
    if not isPresent(list2,i):
        list2.append(i)

print(list2)