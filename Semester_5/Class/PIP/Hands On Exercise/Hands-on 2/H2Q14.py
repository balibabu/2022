'''H2.Q14. Write a python program that takes two int values m and d from the command line and prints 
true if day d of month m is between 3/20 and 6/20, false otherwise.'''
import sys
m=int(sys.argv[1])
d=int(sys.argv[2])
isBetween=(m==3 and 20<d<31)or (m==4 and 0<d<30) or (m==5 and 0<d<31) or (m==6 and 0<d<20)
print('is the given date betwee 3/20 and 6/20 ?'isBetween)

