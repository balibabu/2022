'''4. Write a recursive function to calculate the harmonic sum of first n terms. Note: The
harmonic sum is the sum of reciprocals of the positive integers. For example, if n =
4, the output should be (1+1/2+1/3+1/4 ) = 2.0833'''
def harmonic_sum(n):
    '''harmonic sum of n numbers'''
    if n==1 or n==0:
        return n
    else:
        return 1/n+harmonic_sum(n-1)

n=int(input('enter number of terms:'))
print(harmonic_sum(n))