# a=set()
# a.update('a')
# print(a)
#
# b=list(a)
# print(b)
#
# c=set(b)
# print(c)

# this is really fucking confusing code
def mix(s1,s2,l,r,s=''):
    if l+r==len(s1+s2):
        print(s)
        return
    if l<len(s1):
        mix(s1, s2, l + 1, r,s+s1[l])
    if r<len(s2):
        mix(s1, s2, l, r + 1,s+s2[r])

#mix('abc','def',0,0)


def subsetSum(arr, l, r, sum=0):
    if l > r:
        print(sum)
        return
    subsetSum(arr, l + 1, r, sum+arr[l])
    subsetSum(arr, l + 1, r, sum)

arr=[1,2,3]
subsetSum(arr,0,len(arr)-1)
