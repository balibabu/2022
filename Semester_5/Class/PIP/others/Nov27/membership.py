'''membership function (in)'''
print('a' in 'Python')
print('o' in 'Python')

str='hello'
for ch in str:
    print(ch,end=' ')

print()
'''count method: counting number of letter'''
str='Programming'
print('count=',str.count('g'))
print('count',str.count('r',0,3))

'''find: gives position of first occurance  and rfind: gives the position of last occurance'''
colors='orange,yellow,blue,red,blue,red'
print(colors.find('red'))
print(colors.rfind('red'))
print('===================================================\n\n')
'''capitalize :capitalizes the first letter of a string  || title: capitalizes first letter of all string'''
str='python programming'
print(str.capitalize())
print(str.title())
print('12am'.capitalize())
print('12am'.title())
print('===================================================\n\n')

'''upper  lower   swapcase:capital to small'''
print('12amA'.upper())
print('12Ma'.lower())
print('12am'.swapcase())
print('swapCase'.swapcase())

'''boolean islower() isupper() istitle()'''
str='poWer Zoom canDy'
print(str.isupper())
print(str.islower())
print(str.istitle())
print('paper'.islower())
print('Paper Cook'.istitle())
print('Paper cook'.istitle())


'''strip():removes spaces from start and end
 lstrip(): removes spaces from left
 rstrip(): removes space from right'''
str='   poWer Zoom canDy  '
print(str)
print(str.strip())
print('===================================================\n\n')

'''split'''
print(str.split(' '))
str='bali babu chauhan'
print(str.split(' '))
'''partition splits only once and include regex'''
str='bali babu chauhan'
print(str.partition(' '))
'''booleans returns'''
print('abc'.isalpha()) #true
print('abc1'.isalpha()) #false
print('abc1'.isalnum()) #true
print('12345678'.isdigit())



