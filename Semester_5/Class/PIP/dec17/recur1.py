def sum_of_list(list1):
    if list1==[]:
        return 0
    elif type(list1[0])==list:
        return sum_of_list(list1[0])
    else:
        return list1[0]+sum_of_list(list1[1:])

print(sum_of_list([1,2,3,[1,2,[5,3]]]))
