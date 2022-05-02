def f(s1,s2):
    for i in range(len(s1)):
        for j in range(len(s2)):
            return
        return
    
def f1(s1,s2,k=1):
    if k>len(s1):
        return
    for i in range(len(s2)+1):
        print(s2[0:i]+s1[:k]+s2[i:]+s1[k:])
    f1(s1,s2,k+1)

# f1('ab','cd')
f1('abc','def')



# ‘ABCD’,‘ACBD’, ‘ACDB’, ‘CDAB’, ‘CADB’ and ‘CABD