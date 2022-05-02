from person import Person
from date import Date
class Employee(Person):
    employeeId=1000
    employeeCount=0
    def __init__(self,name,dob,address,doj,salary):
        Person.__init__(self,name,dob,address)
        self.doj=doj
        self.salary=salary
        Employee.employeeId+=1
        Employee.employeeCount+=1
    
    def __str__(self):
        return Person.__str__(self)+'\nemployeeId:'+str(Employee.employeeId)+'\nDate of joing:'+str(self.doj)+'\nSalary:'+str(self.salary)


obj1=Employee('Ram',Date(21,2,2001),'Birgunj',Date(22,12,2020),15000)
print(obj1)