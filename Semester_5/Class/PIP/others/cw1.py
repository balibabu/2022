def titleit(list1):
    list2=[]
    for i in list1:
        a=i[0]
        if ord(i[0])>96:
            a=chr(ord(i[0])-32)
        for j in range(1,len(i)):
            if(ord(i[j])>64 and ord(i[j])<91):
                a+=chr(ord(i[j])+32)
            else:
                a+=i[j]
        list2.append(a)
    print(list2)

titleit(['BaAa','caTiaAz'])
            
           
