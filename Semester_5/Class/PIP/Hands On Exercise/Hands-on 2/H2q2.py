#Write a python program that reads an integer between 0 and 1000 and adds all the digits in the intege
num=int(input("enter a number between 0 and 1000 "))
sum1=num%10
num//=10
sum1+=num%10
num//=10
sum1+=num
print("Sum of digit is ",sum1)
