import os
import re
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for item in listOfFile:
        fullPath = os.path.join(dirName, item)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def readfiles(fname):
    f=open(fname)
    temp= f.read()
    return temp

def isPresent(regex,str1):
	x=re.search(regex,str1)
	return x!=None


x = (getListOfFiles('G:\\My Drive\\Class\\'))

regex = input('enter keyword(regex) ')
count = 0
outcome = list()
for i in x:
    try:
        file = (readfiles(i))
        if isPresent(regex, file):
            outcome.append(i)
            count += 1
            print(count, '=>', i)
    except:
        pass
print('found match:', count)
print('Total file searched:', len(x))
if count == 0:
    print('No matching found')
elif count == 1:
    print(readfiles(outcome[0]))
else:
    while (1):
        choice = int(input('enter an option number or 0 to quit:'))
        if choice == 0: break
        print(readfiles(outcome[choice - 1]))

