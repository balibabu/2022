def harmonic_sum(n):
    '''harmonic sum of n numbers'''
    if n==1 or n==0:
        return n
    else:
        return 1/n+harmonic_sum(n-1)

print(harmonic_sum(3))
