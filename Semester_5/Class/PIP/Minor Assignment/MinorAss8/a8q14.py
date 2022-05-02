'''14. Write a recursive function that deletes every kth element, and returns the modified list.
 For example, if we wish to delete every 3rd element from the list [1, 2, 3, 4, 5,6, 7, 8, 9, 10, 11]
 the output list will be [1, 2, 4, 5, 7, 8, 10, 11]'''

def delete(arr,k):
    if(len(arr)<k):
        return arr
    else:
        return arr[:k-1]+delete(arr[k:],k)

a=eval(input('enter a list\n'))
k=int(input('enter the postion:'))
print(delete(a,k))
