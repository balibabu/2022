'''H2.Q12.Write  a  python  program  that  takes  three  double  values  x,  y,  and  z  as  command-line 
arguments and prints true if the values are strictly ascending or descending (x < y < z or x 
> y > z), and false otherwise.'''

import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
print(a>b>c or a<b<c)
