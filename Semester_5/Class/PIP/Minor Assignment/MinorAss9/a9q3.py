'''3. Write a function that takes data to be stored in the file file1 as interactive input from the user until
he responds with nothing as input. Each line (or paragraph) taken as input from the user should be
capitalized, and stored in the file file1.'''
f1=open("file1.txt","w")
print("write something in file1")
content=input()
while(content!=''):
    f1.write(content.capitalize()+'\n')
    content=input()
f1.close()

'''hi
my name is bali
i am from nepal
i am studying cse
soa is nice place for students
'''