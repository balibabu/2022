'''Write a python program that reads in a set of n single digits and converts them into a single
decimal integer. For example, the program should convert the set of 5 digits {2, 7, 4, 9, 3} to the
integer 27493.'''
def digit_to_num(ndigits):
    print("enter the digits")
    num = 0
    for i in range(ndigits):
        num = num * 10 + int(input())
    return num

ndigits=int(input("enter number of digits "))
print("the number formed is",digit_to_num(ndigits))