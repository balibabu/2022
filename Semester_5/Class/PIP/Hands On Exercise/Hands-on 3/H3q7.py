'''Write a python program that prompts the user to enter the month and year and displays the
number of days in the month. For example, if the user entered month 2 and year 2012, the
program should display that February 2012 had 29 days. If the user entered month 3 and
year 2015, the program should display that March 2015 had 31 days
}'''
def isLeapYear(year):
    if(year%400==0):
        return True
    elif year%4==0 and year%100!=0:
        return True
    return False

def nofdays(month,year):
    m=['','January','Fanuary','March','April','May','June','July','August','September','October','November','December']
    d=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2:
        if isLeapYear(year):
            print(m[2],year,'has 29 days')
        else:
            print(m[2], year, 'has 28 days')
    else:
        print(m[month], year, 'has',d[month],'days')
        
month=int(input('enter month:'))
year=int(input('enter year:'))
nofdays(month,year)
