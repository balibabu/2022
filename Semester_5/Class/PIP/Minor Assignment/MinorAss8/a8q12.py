'''12. Write a recursive function that takes two strings as input parameters and prints all
interleaving strings of the given two strings preserving their order of occurrence. For
example, interleaving of strings ‘AB’ and ‘CD’ will generate the strings: ‘ABCD’,
‘ACBD’, ‘ACDB’, ‘CDAB’, ‘CADB’ and ‘CABD’.'''

def mix(s1,s2,l=0,r=0,s=''):
    if l+r==len(s1+s2):
        print(s)
        return
    if l<len(s1):
        mix(s1, s2, l + 1, r,s+s1[l])
    if r<len(s2):
        mix(s1, s2, l, r + 1,s+s2[r])
        
        
mix(input('enter first string:'),input('enter second string:'))