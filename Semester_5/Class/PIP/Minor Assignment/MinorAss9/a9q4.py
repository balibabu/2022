'''4. Write a function that reads the file file1 and copies only alternative
lines to another file file2. Alternative lines copied should be the
odd numbered lines. Handle all exceptions that can be raised.'''

f1=open("file1.txt","r")
f2=open("file2.txt","w")
content=f1.readline()
while(content!=''):
    f2.write(content)
    content = f1.readline()
    content=f1.readline()
print('copied..')
f1.close()
f2.close()
