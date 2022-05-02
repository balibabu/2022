import random
print('0-scissor, 1-rock, 2-paper')
choice=int(input('choose a number '))
n=random.randint(0,2)
print('computer choose',n)
if n==choice:
    print('draw')
elif (n+1)%3==choice:
    print('you won')
else:
    print('you lose')



