'''11. Write a recursive function that generates all binary strings of n-bit length.
'''
def generate_binary(n,p,str1=''):
    if p>=n:
        print(str1)
        return
    generate_binary(n,p+1,str1[0:p]+'1'+str1[p+1:])
    generate_binary(n,p+1,str1)

n=int(input('enter a number:'))
generate_binary(n,0,n*'0')