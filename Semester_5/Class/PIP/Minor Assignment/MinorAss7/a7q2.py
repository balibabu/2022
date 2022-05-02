# Write a function that takes a list of numbers as input from the user and produces the corresponding
# cumulative list where each element in the list at index i is the sum of elements at index j <= i.
list1 = []
list2 = []
print('enter int value in list')
for i in range(10):
    list1.append(int(input()))

list2.append(list1[0])
for i in range(1,len(list1)):
    list2.append(list2[i-1]+list1[i])

print(list1)
print(list2)