class Employee:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def __str__(self):
        return 'Name:'+self.name+'\nDate of birth:'+self.dob

class Clerk(Employee):
    def __init__(self,name,dob):
        Employee.__init__(self,name,dob)
    def __del__(self):
        del self
    def __str__(self):
        return Employee.__str__(self)

class Manager(Employee):

