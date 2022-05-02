'''6. Write a function that reads the contents of the file Poem.txt and counts the number of alphabets, blank
spaces, lowercase letters and uppercase letters, the number of words starting with a vowel, and the
number of occurrences of word ’beautiful’ in the file.'''
def no_of_words_a(sentence):
    words=sentence.split()
    count=0
    for i in words:
        if i[0] in 'aeiouAEIOU':
            count+=1
    return count

f=open('Poem.txt','r')
text = f.read()
print(text)
alpha,lcase,ucase,space=0,0,0,0
for i in text:
    if(i.isalpha()):
        alpha+=1
        if(i.islower()):
            lcase+=1
        else:
            ucase+=1
    elif (i.isspace()):
        space+=1

print('no. of alphabets is',alpha)
print('no. of blank spaces is',text.count(' '))
print('no. of upper letters is',ucase)
print('no. of lower letters is',lcase)
print('no. of words starting with vowel is',no_of_words_a(text))
f.close()