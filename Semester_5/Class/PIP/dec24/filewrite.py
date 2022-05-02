f1=open("file1.txt","w")
print("write something in file1")
content=input()
while(content!=''):
    f1.write(content+'\n')
    content=input()
f1.close()
