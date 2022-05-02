def reverse_string(string):
    '''Reverse a string'''
    a=''
    for i in string:
        a=i+a
    return a

def reverse_string_wordwise(string):
    '''Reverse a string without reversing the words'''
    a=''
    words=string.split(' ')
    for i in words:
        a=i+' '+a
    return a[:-1] # to remove the extra space

def isSymmetric(string):
    '''Check if a string is symmetric or asymmetric'''
    half = len(string)//2
    if len(string)%2:
        return string[:half]==string[half+1:]
    return string[:half]==string[half:]


def isPalindrome(string):
    '''Check if a string is palindrome.'''
    a=reverse_string(string)
    return a==string

def delete_char(string,pos):
    '''Given a string s and index i, delete ith value from s'''
    return string[:pos]+string[pos+1:]

def vowels(string):
    '''Count the number of vowels and consonants in a string'''
    vow=0
    cons=0
    for i in string:
        if i.isalpha():
            i=i.lower()
            if i in 'aeiou': vow+=1
            else: cons+=1
    print('no. of vowels is',vow)
    print('no. of consonants is',cons)
def getLength(string):
    '''Find length of a string without using inbuilt function.'''
    c=0
    for i in string:
        c+=1
    return c
def atleastalnum(string):
    '''Check if a string contains at least one digit and one alphabet'''
    a,d=0,0
    for i in string:
        if i.isalpha(): a+=1
        if i.isdigit(): d+=1
        if a and d: return True
    return False
def remove_duplicates(string):
    '''Remove duplicates from a string.'''
    def isPresent(string, value):
        for i in string:
            if value == i: return True
        return False
    a=''
    for i in string:
        if not isPresent(a,i):
            a+=i
    return a
def char_frequency(string):
    ''' Count frequency of characters in a string.'''
    temp=remove_duplicates(string)
    list1=list()
    for i in temp:
        print('No. of',i,'is',string.count(i))  #count function: string.count(char)
def get_max_freq_char(string):
    ''' Find the character having maximum frequency in a string.'''
    a=string[0]
    for i in string:
        if string.count(i)>string.count(a): a=i
    return a

def are_Anagrams(str1, str2):
    '''Check if a pair of strings are anagram to each other. Example: SILENT and LISTEN are anagrams.'''
    for i in str1:
        if str1.count(i) != str2.count(i):
            return False
    return True

string="bunbun"
print(reverse_string(string))
print(reverse_string_wordwise(string))
print('is it symmetric?',isSymmetric(string))
print('is it palindrome?',isPalindrome(string))
print(delete_char(string,2))
vowels(string)
print(getLength(string))
print(string.isalnum())
print(atleastalnum(string))
print(remove_duplicates(string))
char_frequency(string)
print(get_max_freq_char(string))
print(are_Anagrams('SILENT','LISTEN'))
