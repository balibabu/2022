# Write a function that takes a string as an input and determines the count of the number of words
# without using regular expression.
def nof_words(string):
    string = string.strip()
    if string=='': return 0
    i=0
    for i in range(len(string)):
        if string[i]==' ':break
    return 1+nof_words(string[i+1:])

sentence=input("enter a sentence\n")
print('Number of words is',nof_words(sentence))