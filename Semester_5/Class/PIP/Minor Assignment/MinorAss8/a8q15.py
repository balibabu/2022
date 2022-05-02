'''Write a recursive function that recursively removes adjacent duplicates from a given
list, and returns the modified list. For example, removing adjacent duplicates recursively
from the list [1, 2, 4, 4, 5, 7, 7, 7, 8, 8, 9, 7] will yield list [1, 2, 5, 9,7].'''
def duplicates(lst):
    if len(lst)<=1:
        return lst
    i=1
    while(lst[0]==lst[i]):
        i+=1
    if(i==1):
        return [lst[0]]+duplicates(lst[i:])
    return duplicates(lst[i:])
    
lst=eval(input('enter a list\n'))
print(duplicates(lst))
# [1, 2, 4, 4, 5, 7, 7, 7, 8, 8, 9, 7]