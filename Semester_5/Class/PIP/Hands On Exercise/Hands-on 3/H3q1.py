'''Input an integer through the keyboard. Write a python program to find out whether it is an
odd number or even number.'''
def even_odd(n):
    if n%2==0: return 'Even'
    return 'Odd'

num=int(input('enter a number:'))
print('the entered number is:',even_odd(num))
