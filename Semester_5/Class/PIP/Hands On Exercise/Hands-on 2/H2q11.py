'''H2.Q11.Write a python program that prints the sum of two random integers between 1 and 6 (such 
as you might get when rolling dice).'''

import sys
import random

rand1=random.randint(1,6)
rand2=random.randint(1,6)
print('the sum of two random integers between 1 and 6 is',(rand1+rand2))
