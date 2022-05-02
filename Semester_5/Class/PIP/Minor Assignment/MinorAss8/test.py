def subsetSum(arr,l,r,sum=[]):
    if l>r:
        print(sum)
        return
    subsetSum(arr,l+1,r,sum)
    subsetSum(arr, l + 1, r, sum)
arr=[2,4,5]
n=len(arr)
subsetSum(arr,0,n-1)

