'''5. Write a function that takes two files of equal size as input from the user. The first
file contains weights of items and the second file contains corresponding prices. Create
another file that should contain price per unit weight for each item.'''

n=int(input('enter no. of items '))
f1=open("file1.txt","w")
f2=open("file2.txt","w")
f3=open("file3.txt","w")
for i in range(n):
    w=input('enter weight ')
    p=input('enter price ')
    f1.write(w+'\n')
    f2.write(p+'\n')
    f3.write(str(int(w)/int(p))+'\n')
f1.close()
f2.close()
f3.close()
print('Done...')