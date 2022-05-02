'''If the ages of Rahul, Ayush and Ajay are input through the keyboard, write a python program
to determine the elder among them.'''

rahul=int(input('enter Rahul\'s age '))
ayush=int(input('enter Ayush\'s age '))
ajay=int(input('enter Ajay\'s age '))
if ajay<rahul>ayush:
    print('Rahul is elder one')
elif ajay<ayush>rahul:
    print('Ayush is elder one')
elif rahul<ajay>ayush:
    print('Ajay is elder one')
else:
    print('some ages are same')