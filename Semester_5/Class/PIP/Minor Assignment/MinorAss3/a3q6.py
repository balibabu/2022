def pattern_a(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        print()
    print('\n')
def pattern_b(n):
    for i in range(n):
        print(" "*((n-i)*2),end="")
        for j in range(i+1,0,-1):
            print(j,end=" ")
        for k in range(2,i+2):
            print(k,end=" ")
        print()
    print('\n')

def pattern_c(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
    print('\n')

def pattern_d(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print()
    print('\n')

def pattern_e(n):
    for i in range(1,n+1):
        print(" "*((i-1)*2),end="")
        for j in range(i,n+1):
            print(j,end=" ")
        print()
    print('\n')

def pattern_f(n):
    if n==1:
        print('*')
    else:
        print('* '*n)
        for i in range(n-2):
            print('{}{}{}'.format('*',' '*(n*2-3),'*'))
        print('* ' * n)
    print('\n')

def pattern_g(n):
    for i in range(n):
        print('* '*n)
    print('\n')

def pattern_h(n):
    for i in range(1,n+1):
        print(" " * ((n - i) * 2), end="")
        for j in range(i*2-1):
            print('* ',end='')
        print()
    print('\n')

def pattern_i(n):
    if n==1:
        print('*')
    elif n>1:
        print('* '*(n*2-1))
        for i in range(n-2):
            print(' '*(i*2+1),'*',' '*(n*4-3-(4*(i+1)+4)),'*')
        print(' '*(n*2-3),'*')
    print('\n')

def pattern_j(n):
    for i in range(n):
        print(' '*(i*2),'* '*(n*2-1-i*2))
    print('\n')

def pattern_k(n):
    print(" " * (n * 2), '*')
    for i in range(n-1):
        print(" " * ((n - i-1) * 2),'*',' '*(4*i+1),'*')
    for i in range(n-2,0,-1):
        print(" " * ((n - i ) * 2), '*', ' ' * (4 * i -3), '*')
    print(" " * (n * 2 ), '*')
    print('\n')

def pattern_l(n):
    for i in range(1, n + 1):
        print(" " * ((n - i) * 2), end="")
        for j in range(i * 2 - 1):
            print('* ', end='')
        print()
    for k in range(n-1):
        print(' ' * (k * 2+1), '* ' * (n * 2 - 3 - k * 2))
    print('\n')

def pattern_m(n):
    for i in range(1,n+1):
        print(" "*((i-1)*2),end="")
        for j in range(i,n+1):
            print('$',end=" ")
        print()
    print('\n')

def pattern_n(n):
    for i in range(n):
        print(" "*((n-i)*2),end="")
        for j in range(i+1,0,-1):
            print('#',end=" ")
        print()
    print('\n')

num=int(input("enter number of rows "))
pattern_a(num)
pattern_b(num)
pattern_c(num)
pattern_d(num)
pattern_e(num)
pattern_f(num)
pattern_g(num)
pattern_h(num)
pattern_i(num)
pattern_j(num)
pattern_k(num)
pattern_l(num)
pattern_m(num)
pattern_n(num)
