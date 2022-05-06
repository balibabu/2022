stringlist1=eval(input('enter a list of names '))


name_occurence={name:stringlist1.count(name) for name in stringlist1}
Mstringlist1=[name for name in name_occurence]
print("Mstringlist1 ",Mstringlist1)


word=input('enter a word from the list ')
if(name_occurence[word]%2):
    print(f'{word} has odd occurence')
else:
    print(f'{word} has even occurence')
    
i=0
while(i<len(stringlist1)):
    j=i+1
    while(j<len(stringlist1)):
        if stringlist1[i]==stringlist1[j]:
            stringlist1.pop(j)
        j+=1
    i+=1

print("stringlist1 ",stringlist1)
