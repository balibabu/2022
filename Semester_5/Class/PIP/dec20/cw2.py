def duplicates(lst):
    '''remove the adjacent duplicates using recursion'''
    if len(lst)==1 or len(lst)==0:
        return lst
    else:
        if lst[0]==lst[1]:
            return lst[:1]+duplicates(lst[2:])
        return lst[:1]+duplicates(lst[1:])
print(duplicates([1,1,2,2,3]))
