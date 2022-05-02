# Write a program that takes a sentence as input from the user and computes the frequency of each
# letter. Use a variable of dictionary type to maintain the count.
def isPresent(list,value):
    for i in list:
        if value==i: return True
    return False

str1=input('enter a sentence: ')
str2=''
for i in str1:
    if not isPresent(str2,i) and i !=' ':
        str2+=i

for i in str2:
    print(i,'-->',str1.count(i))