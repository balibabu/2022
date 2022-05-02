import pdb

pdb.set_trace()
def summation(n):
    total=0
    for count in range(1,n):
        total+=count
    return total

def main():
    n=int(input('enter the number of terms: '))
    total=summation(n)
    print('sum of first',n,'numbers is:',total)

if __name__=='__main__':
    main()

# r,h,p,(u,d),n,s,p,l,q
