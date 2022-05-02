'''10. Find the sum of even digits of a four-digit number using function.
Warning: Don’t use control structures.'''
def get_sum_even_digit(num):
    sum1=0
    d=num%10
    sum1+=((d+1)%2)*d
    
    num=num//10
    d=num%10
    sum1+=((d+1)%2)*d
        
    num=num//10
    d=num%10
    sum1+=((d+1)%2)*d
    
    num=num//10
    d=num%10
    sum1+=((d+1)%2)*d
    
    return sum1

print(get_sum_even_digit(2345))
    
