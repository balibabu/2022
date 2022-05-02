class Students:
    marksList=[]

    def __init__(self,rollNum,name,stream):
        self.rollNum=rollNum
        self.name=name
        self.stream=stream

    def setMarks(self):
        print('enter marks for five subject')
        for i in range(5):
            self.marksList.append(int(input('enter marks:')))

    def getStream(self):
        dict={'A':'Arts','C':'Commerce','S':'Science'}
        return dict[self.stream]

    def getPercentage(self):
        return sum(self.marksList)/5

    def gradeGen(self):
        def getGrade(mark):
            if mark>=90: return 'A'
            elif mark>=80: return 'B'
            elif mark>=65: return 'C'
            elif mark>=40: return 'D'
            else: return 'E'
        for i in range(5):
            print('grade in subject {} is {}'.format(i+1,getGrade(self.marksList[i])))

s1=Students(int(input('enter your roll no.')),input('enter your name:'),input('enter stream:'))
s1.setMarks()
print(s1.getStream())
print(s1.getPercentage())
s1.gradeGen()
