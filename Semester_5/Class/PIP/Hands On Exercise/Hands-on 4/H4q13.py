'''Write a python program that puts the binary representation of a positive integer N into a String s.'''
def binary_string(num):
    s=''
    while num>0:
        s=str(num%2)+s
        num//=2
    return s

num=int(input("enter a number in decimal form "))
print("the number in binary form is",binary_string(num))
