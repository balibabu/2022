import random
def generatePassword(size):
    password=''
    for i in range(size):
        cap_small_digit=random.choice([48,65,97])
        if cap_small_digit == 48:
            digit=48+random.randrange(10)
            password+=chr(digit)
        else:
            letter=cap_small_digit + random.randrange(26)
            password+=chr(letter)
    return password
        
def saveInFile(list1:list,filename='MyPasswords.txt'):
    f=open(filename,'w')
    for i in list1:
        f.write(i+'\n')
    f.close()
    print('your password has been saved in MyPasswords.txt')

no_of_pwd=int(input('how many pwd you wanna generate: '))
pwd_list=[]
for i in range(no_of_pwd):
    pwd_list.append(generatePassword(int(input('enter size of password: '))))
saveInFile(pwd_list)