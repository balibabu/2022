'''2. Write a function that reads a file file1 and displays the number of words and the number of vowels in
the file.'''
def vowels(string):
    '''Count the number of vowels and consonants in a string'''
    vow=0
    for i in string:
        if i in "aeiouAEIOU":
            vow+=1
    print('no. of vowels is',vow)

def no_of_words(sentence):
    print("number of words =",len(sentence.split()))
    
f=open('file1.txt','r')
temp=f.read()
print(temp)
vowels(temp)
no_of_words(temp)