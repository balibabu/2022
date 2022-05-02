'''H2.Q9. Write a python program that takes two positive integers as command-line arguments and 
prints true if either evenly divides the other.
'''

import sys
def main():
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    assert a>0 and b>0, "do not give negative number"
    print((a%b==0 or b%a==0))


main()
