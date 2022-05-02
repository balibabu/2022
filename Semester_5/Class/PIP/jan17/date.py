class Date:
    def __init__(self,dd,mm,yyyy):
        self.dd=dd
        self.mm=mm
        self.yyyy=yyyy
    def __str__(self):
        return str(self.dd)+'/'+str(self.mm)+'/'+str(self.yyyy)

