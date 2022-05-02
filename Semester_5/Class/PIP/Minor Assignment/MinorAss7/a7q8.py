'''Given the following inputs, indicate in each case (a) to (w), whether the statements will execute
successfully. If, so, give what will be the outcome of execution? Also give the output of print
statements (where applicable):'''
address = 'B-6, Lodhi road, Delhi'
list1 = [1, 2, 3]
list2 = ['a', 1, 'z', 26, 'd', 4]
tuple1 = ('a', 'e', 'i', 'o', 'u')
tuple2 = ([2,4,6,8], [3,6,9], [4,8], 5)
dict1 = {'apple': 'red', 'mango': 'yellow', 'orange': 'orange'}
dict2 = {'X': ['eng', 'hindi', 'maths','science'], 'XII': ['english', 'physics', 'chemistry', 'maths']}

#list1[3]=4 #list assignment index out of range

# print(list1*2)

#print(min(list2))  #we can't compare betn int and char

# print(max(list1))
#
# print(list(address)) #make list with each chars
#
# list2.extend(['e', 5])
# print(list2)
#
# list2.append(['e', 5])
# print(list2)
#
# names = ['rohan', 'mohan', 'gita']
# names.sort(key= len)
# print(names)
#
# list3 = [(x * 2) for x in range(1, 11)]
# print(list3)
#
# del list3[1:]
# print(list3)
#
# list4 = [ x+y for x in range(1,5) for y in range(1,5)]
# print(list4)
#
#tuple2[3] = 6  #'tuple' object does not support item assignment
#tuple2.append(5)  #no attribute 'append'
# #t1 = tuple2 +(5)   #can only concatenate tuple (not "int") to tuple
# t1 = tuple2 +(5,)
# ','.join(tuple1)    #type is string
# print(','.join(tuple1))
#
# print(list(zip(['apple', 'orange'], ('red','orange')))) #zip returns tuple
#
# print(dict2['XII'])
#
# dict2['XII'].append('computer science'),dict2
# print(dict2)
#
# print('red' in dict1)  #give string is key for dictionary
# print(list(dict1.items()))
# print(list(dict2.keys()))
# print(dict2.get('XI', 'None'))
#
# dict1.update({'kiwi':'green'})
# print(dict1)