f1=open("file1.txt","r")
f2=open("file2.txt","w")

content=f1.readline()
while(content!=''):
    f2.write(content)
    content=f1.readline()
f1.close()
f2.close()
