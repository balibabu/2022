def isArmstrong(n):
    sumd=0
    temp=n
    while(n):
        sumd+=(n%10)**3
        n//=10
    return sumd==temp

for i in range(1,1000):
    if(isArmstrong(i)):
        print(i,end=' ')