def vowels(string):
    '''Count the number of vowels and consonants in a string'''
    vow=0
    for i in string:
        if i in "aeiouAEIOU":
            vow+=1
    print('no. of vowels is',vow)

def no_of_words(sentence):
    print("number of words =",len(sentence.split()))




f=open("file1.txt","r")
string=f.read()
print(string)
no_of_words(string)
vowels(string)
f.close()
