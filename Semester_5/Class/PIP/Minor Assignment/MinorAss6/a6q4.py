# Write a function that takes a sentence as an input parameter and replaces the first letter of every word
# with the corresponding uppercase letter and rest of the letters in the word by corresponding letters in
# lowercase without using builtin function.

def titleit(string):
    a=string[0]
    if(ord(a)>96 and ord(a)<123):
        a=chr(ord(string[0])-32)
    for i in range(1,len(string)):
        if string[i-1]==' ':
            if ord(string[i])>96 and ord(string[i])<123:
                a+=chr(ord(string[i])-32)
            else:
                a+=string[i];
        else:
            if ord(string[i])>64 and ord(string[i])<91:
                a+=chr(ord(string[i])+32)
            else:
                a+=string[i];
    return a


sentence=input("enter a sentence\n")
print(titleit(sentence))