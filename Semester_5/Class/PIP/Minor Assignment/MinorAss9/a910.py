#a
try:
    f = open('file1', 'r')
except IOError:
    print('Problem with Input Output...\n')
else:
    print('No Problem with Input Output...')
    
    
#b
try:
    f = open('file1', 'w')
except IOError:
    print('Problem with Input Output...\n')
else:
    print('No Problem with Input Output...\n')