'''Write a function that takes a number as an input parameter and returns the correspond text in words,
for example, on input 452, the function should return ’Four Five Two’. Use a dictionary for mapping
digits to their string representation.'''
def getString(num):
    numbers = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',9: 'Nine'}
    a=''
    while num>0:
        a=numbers[num%10]+' '+a
        num//=10
    return a

num=int(input('enter a number: '))
print(getString(num))



