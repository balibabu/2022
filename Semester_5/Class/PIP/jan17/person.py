class Person:
    def __init__(self,name,dob,address):
        self.name=name
        self.dob=dob
        self.address=address

    def __str__(self):
        return 'Name:'+self.name+'\nDate of birth:'+str(self.dob)+'\nAddress:'+self.address