'''
Define a base cla_s%ahj.cle, having attributes regi sl;atio‘n number, make, model, and colour. Alsg,
define classes PassengerVehicle and Commercial Vehicle that derive from the class Vehicle. The Pas”
sengerVehicle class should have additional attribute for maximum passenger capa'c-iT_'y, The Com-
mercial Vehicle class should have an additional attribute for maximum load capacity. Define __init__
method for all these classes. Also, define get and set methods to retrieve and set the value of the Jata
attributes. m dasd
'''

class Vehicle:
    def __init__(self,rg_no,make,model,color):
        self.rg_no=rg_no
        self.make=make
        self.model=model
        self.color=color
    def setRegistrationNo(self,rg_no):
        self.rg_no
    def setMake(self,make):
        self.make=make
    def setModel(self,model):
        self.model=model
    def setColor(self,color):
        self.color=color
    def getRegistrationNo(self):
        return self.rg_no
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getColor(self):
        return self.color
    def __str__(self):
        return 'Registration No.:'+str(self.rg_no)+' Make:'+str(self.make)+' Model:'+str(self.model)+' Color:'+(self.color)

class PassengerVehicle(Vehicle):
    def __init__(self, rg_no, make, model, color,maxp):
        Vehicle.__init__(self,rg_no, make, model, color)
        self.maxp=maxp
    def setMaxPassengerCapacity(self,maxp):
        self.maxp=maxp
    def getMaxPassengerCapacity(self):
        return self.maxp
    def __str__(self):
        return Vehicle.__str__(self)+' Max. Passenger:'+str(self.maxp)

class CommercialVehicle(Vehicle):
    def __init__(self,rg_no, make, model, color,maxl):
        Vehicle.__init__(self,rg_no, make, model, color)
        self.maxl=maxl
    def setMaxLoadCapacity(self,maxl):
        self.maxl=maxl
    def getMaxLoadCapacity(self):
        return self.maxl
    def __str__(self):
        return Vehicle.__str__(self)+' Max. Load Capacity:'+str(self.maxl)

def main():
    # rg_no, make, model, color,maxp
    v1=PassengerVehicle(1234,'ABC','xyz','Red',30)
    print(v1.getMake())
    print(v1.getRegistrationNo())
    print(v1.getMaxPassengerCapacity())
    print(v1)

    v2=CommercialVehicle(1255,'ABC','xyz','Red',30000)
    print(v2.getMake())
    print(v2.getRegistrationNo())
    print(v2.getMaxLoadCapacity())
    print(v2)

if __name__=='__main__':
    main()































'''    def setRegistrationNo(self, rg_no):
        Vehicle.setRegistrationNo(self,rg_no)

    def setMake(self, make):
        Vehicle.setMake(self,make)

    def setModel(self, model):
        Vehicle.setModel(self, model)

    def setColor(self, color):
        Vehicle.setColor(self, color)

    def getRegistrationNo(self):
        return Vehicle.getRegistrationNo(self)

    def getMake(self):
        return Vehicle.getMake(self)

    def getModel(self):
        return Vehicle.getModel(self)

    def getColor(self):
        return Vehicle.getColor(self)'''