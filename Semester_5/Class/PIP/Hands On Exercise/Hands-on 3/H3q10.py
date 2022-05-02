'''A University conducts a 100 mark exam for its student and grades them as follows. Assigns
a grade based on the value of the marks. Write a python program to print the grade
according to the mark secured by the student.'''

def get_grade(mark):
    if mark>100:
        return ('not valid')
    elif mark>=90:
        return 'O'
    elif mark>=80:
        return 'A'
    elif mark>=70:
        return 'B'
    elif mark>=60:
        return 'C'
    elif mark>=50:
        return 'D'
    elif mark>=40:
        return 'E'
    else:
        return 'F'

mark=int(input("enter your marks "))
print('your grade is',get_grade(mark))