'''H2.Q10.Write a python program that takes two int values a and b from the command line and prints 
a random integer between a and b.'''
import sys
import random
a=int(sys.argv[1])
b=int(sys.argv[2])
rand=random.randint(a,b)
print('Random value between ',a,'and',b,'is',rand)
