def isPerfect(num):
    if num==1: return True
    sum1=0
    for i in range(1,num//2+1):
        if(num%i==0): sum1+=i
    return sum1==num

num=int(input('enter a number '))
print('Is it perfect number?',isPerfect(num))
