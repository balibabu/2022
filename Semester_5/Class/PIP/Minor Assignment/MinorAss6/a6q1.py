def replace_repeated(str1):
    temp=''
    for i in str1:
        if temp==i:
            print('*',end='')
        else:
            print(i,end='')
        temp=i
        


str1=input('enter a  string ')
replace_repeated(str1)
