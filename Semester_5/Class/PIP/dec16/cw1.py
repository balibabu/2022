def getOccurence(string):
    d=dict()
    for i in string:
        d[i]=string.count(i)

    print(d)


getOccurence(input('enter a string: '))
