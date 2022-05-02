'''8. Construct logical expressions for representing the following conditions:
a. marks scored should be greater than 300 and less than 400.
b. Whether the value of grade is an uppercase letter.
c. The post is engineer and experience is more than four years'''
marks=int(input('enter your mark '))
if 300<marks<400:
    print(True)
else:
    print(False)

grade=input('enter your grade ')[0]
if grade<='Z':
    print('Uppercase')
else:
    print('Lowercase')

post=input('enter your post ')
exp=int(input('enter your experience '))
if post.lower()=='engineer' and exp > 4:
    print(True)
else:
    print(False)

