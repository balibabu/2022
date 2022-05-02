ndigits=int(input("enter number of digits "))
print("enter the digits")
num=0
for i in range(ndigits):
    num=num*10+int(input())

print("the number formed is",num)
