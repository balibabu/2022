'''1. Write a function that takes two file names, file1 and file2 as input. The function should read the contents of the file file1 line by line and should write them to another file file2 after adding a newline at
the end of each line.'''

f1=open("file1.txt","w")
print("write something in file1")
content=input()
while(content!=''):
    f1.write(content+'\n')
    content=input()
f1.close()


f1=open("file1.txt","r")
f2=open("file2.txt","w")
content=f1.readline()
while(content!=''):
    f2.write(content+'\n')
    content=f1.readline()
f1.close()
f2.close()

