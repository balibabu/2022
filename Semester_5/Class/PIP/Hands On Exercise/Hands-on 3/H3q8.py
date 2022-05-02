'''Write a python program that plays the popular scissor-rock-paper game. (A scissor can cut
a paper, a rock can knock a scissor, and a paper can wrap a rock.) The program randomly
generates a number 0, 1, or 2 representing scissor, rock, and paper. The program prompts
the user to enter a number 0, 1, or 2 and displays a message indicating whether the user or
the computer wins, loses, or draws.'''

import random
arr=['scissor', 'rock', 'paper']
print('0-scissor, 1-rock, 2-paper')
choice=int(input('choose a number '))
n=random.randint(0,2)
print('you choose',arr[choice])
print('computer choose',arr[n])
if n==choice:
    print('draw')
elif (n+1)%3==choice:
    print('you won')
else:
    print('you lose')