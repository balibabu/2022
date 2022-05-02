def are_Anagrams(str1,str2):
    for i in str1:
        if str1.count(i)!=str2.count(i):
            return False
    return True

str1=input('enter 1st string ')
str2=input('enter 2nd string ')
print('Are both string anagrams?',are_Anagrams(str1,str2))
