'''7. Write a recursive function to print the sums of all the subsets of a given array.
For Example: Input: lst = [2,3] Output:0,2,3,5. Input: lst = [2,4,5] Output:0,2,4,5,6,7,9,11.
'''
def subsetSum(arr,l,r,sum=0):
    if l>r:
        print(sum,end=' ')
        return
    subsetSum(arr,l+1,r,sum)
    subsetSum(arr, l + 1, r, sum + arr[l])

arr=[2,4,5]
n=len(arr)
subsetSum(arr,0,n-1)


















# def sum_subsets(arr,n):
#     t=1<<n
#     for i in range(t):
#         Sum=0
#         for j in range(n):
#             if((i&(1<<j))!=0):
#                 Sum+=arr[j]
#         print(Sum,end=' ')

# sub([2,4],2)