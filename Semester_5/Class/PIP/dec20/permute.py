def permute(list1,list2=[],k=0,pos=0):
    list2.insert(pos,list1[k])
    if len(list1)==len(list2):
        print(list2)
    else:
        
