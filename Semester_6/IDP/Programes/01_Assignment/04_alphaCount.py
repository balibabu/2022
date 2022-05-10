def count(content):
    tempDict={chr(i):0 for i in range(97,123)}
    freqDict={}
    for i in content:
        i=i.lower()
        if i in tempDict:
            tempDict[i]+=1
    for i in tempDict:
        if tempDict[i] != 0:
            freqDict[i]=tempDict[i]
    return freqDict

def readFileNdo(filename='MyText.txt'):
    f=open(filename,'r')
    content=f.read()
    uniqueL=count(content)
    for i in uniqueL:
        print(f'The character “{i}” is present {uniqueL[i]} times in the document.')
    f.close()

readFileNdo()