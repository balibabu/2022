'''Write a function that takes a string as an input and determines the count of the number of words
without using regular expression.'''

def nof_words(string):
    string = string.strip()
    if string=='': return 0
    pos=0
    c=1
    temp = string[0]
    for i in string:
        if (i>='A' and i<='Z') or (i>='a' and i<='z'):
            print(i)
            temp = string[0]
            pos+=1
            break

    while(pos<len(string)):
        if string[pos]==' ':
            temp=' '
        if (string[pos]>='A' and string[pos]<='Z') or (string[pos]>='a' and string[pos]<='z'):
            if temp==' ':
                c+=1
                temp=string[pos]
            #temp=string[pos]
        pos+=1
    return c



print(nof_words('. a bc  adf chauhan   . .   bali babu .'))