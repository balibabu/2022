def flatter(list1,list2):
    '''to flatter the elements of the list'''
    if list1==[]:
        pass
    elif type(list1[0])==list:
        flatter(list1[0],list2)
        flatter(list1[1:], list2)
    else:
        list2.append(list1[0])
        flatter(list1[1:],list2)

list1=[[1,2,3,[11,[111],12]],1,3,[4]]
list2=[]
flatter(list1,list2)
print(list2)
