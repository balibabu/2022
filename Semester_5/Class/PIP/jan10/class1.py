class Student:
    name=None
    roll=None
s1=Student()
s1.name='ram'
s1.roll=1
print(s1.name)
print(s1.roll)
Student.name='Shyam'
print(Student.name)