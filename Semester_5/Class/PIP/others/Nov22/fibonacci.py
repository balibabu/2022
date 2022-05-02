num=int(input("enter no. of term "))
a,b=0,1;
if(num==1):
    print(a)
elif(num==2):
    print(b)
else:
    print(a)
    for i in range(1,num+1):
        temp=a
        a=a+b
        b=temp
        print(a)



#0,1,1,2,3,5,8,13,21,..
