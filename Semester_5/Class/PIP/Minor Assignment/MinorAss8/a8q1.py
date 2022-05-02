'''1. Write a recursive function that converts a number inputted in string form
to an integer type. For example, if input string is: ‘1234’ then the recursive function should
convert it to 1234(int type)'''
def toInteger(str1):
    if str1=='': return 0
    return toInteger(str1[:-1])*10+int(str1[-1])


a=toInteger(input('enter integer string:'))
print(a,type(a))
