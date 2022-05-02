import pdb
pdb.set_trace()
def findHCF(n1,n2):
    if n1<n2:
        min1=n1
    else:
        min2=n2
    for i in range(min1,1,-1):
        if n1%i==0 and n2%i==0:
            hcf=i
        return hcf

def main():
    print(findHCF(8,12))
