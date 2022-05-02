'''
8. Define classes Car, Autorickshaw, and Bus which derive from the PassengerVehicle class mentioned
in the previous question. The Car and Bus should have attributes for storing information about the
number of doors, not shared by Autorickshaw. The Bus should have Boolean attribute doubleDecker
not shared by Car and Autorickshaw. Define init method for all these classes. Also, define get and
set methods to determine and set the value of the data attributes.
'''
from a11q7 import PassengerVehicle

class Car(PassengerVehicle):
    def __init__(self,rg_no,make,model,color,maxp,no_doors):
        super().__init__(rg_no,make,model,color,maxp)
        self.no_doors=no_doors
    def setNofDoors(self,n):
        self.no_doors=n
    def getNofDoors(self):
        return self.no_doors
    def __str__(self):
        return super().__str__()+' No. of doors:'+str(self.no_doors)

class Autorickshaw(PassengerVehicle):
    def __init__(self,rg_no,make,model,color,maxp):
        super().__init__(rg_no,make,model,color,maxp)

class Bus(Car):
    def __init__(self, rg_no, make, model, color, maxp, no_doors,doubleDecker):
        super().__init__(rg_no, make, model, color, maxp,no_doors)
        self.doubleDecker=doubleDecker
    def setIsdoubleDecker(self,t):
        self.doubleDecker=t
    def getIsdoubleDecker(self):
        return self.doubleDecker
    def __str__(self):
        return super().__str__() + ' isdoubleDecker:' + str(self.doubleDecker)

c=Car(1941,'Tesla','Model3','white',6,4)
print(c)
print()
a=Autorickshaw(1112,'Ola','rocket','black',4)
print(a)
print()
b=Bus(1942,'Scorpio','panther','yellow',40,2,True)
print(b)