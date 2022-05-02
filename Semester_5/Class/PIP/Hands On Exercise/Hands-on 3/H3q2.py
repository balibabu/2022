'''Any character is entered through the keyboard, write a python program to determine 
whether the character entered is a capital letter, a small case letter, a digit or a special 
symbol. The following table shows the range of ASCII values for various characters.
Characters ASCII Values 
A – Z 65 – 90 
a – z 97 – 122 
0 – 9 48 – 57 
special symbols 0 - 47, 58 - 64, 91 - 96, 123 – 127'''
def char_type(c):
    if 'A'<=c<='Z':
        print('capital case letter')
    elif 'a'<=c<='z':
        print('small case letter')
    elif  47<ord(c)<58:
        print('a digit')
    elif 0<=ord(c)<48 or 58 <=ord(c)<= 64 or 91 <=ord(c)<= 96 or 123 <=ord(c)<= 127:
        print('special character')
        
c=input('enter a character ')
char_type(c)
