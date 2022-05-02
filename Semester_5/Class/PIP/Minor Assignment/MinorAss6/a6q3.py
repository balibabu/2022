def no_of_words(sentence):
    sentence=sentence.strip()
    c=sentence.count(' ')
    return c+1

sentence=input('enter a sentence\n')
print('number of words is ',no_of_words(sentence))
