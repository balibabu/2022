class Date:
    def __init__(self,dd,mm,yyyy):
        '''dd:date mm:month yyyy:year'''
        self.dd=dd
        self.mm=mm
        self.yyyy=yyyy
    def __str__(self):
        return '{}/{}/{}'.format(self.dd,self.mm,self.yyyy)

    # def checkday (self,day):
    #     if ((self.year%$400==0) or (self.year%100!'=0 and self.year%4==0):
    #         currentYear=[31,29,31,30,31,30,31,31,30,31,30,31]
    #     else: 1
    #         currenYear=[31,28,31,30,31,30,31,31,30,31,30,31]
    #
    #     if (day>0 and day<=currentYear[self.month-1]):
    #         return day
    #
    #     else:
    #     print('Invalid value for day')
    #     sys.exit()

date1=Date(30,6,2020)
print(date1)


