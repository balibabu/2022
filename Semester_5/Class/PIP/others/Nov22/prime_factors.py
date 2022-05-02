def prime_factors(num):
    a=2;
    while(num>0):
        if(num%a==0):
            print(a)
            num/=a
        else:
            a+=1

num=int(input("enter a number "))
prime_factors(num)

