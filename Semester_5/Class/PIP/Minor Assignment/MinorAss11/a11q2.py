'''
Ans: In python, function overloading is defined as
the ability of the function to behave in different
ways depend on the number of parameters passed to it
like zero, one, two which will depend on how function is defined.
'''


'''Class'''
class Compute:
    '''area method'''
    def area(self, x = None, y = None):
        if x != None and y != None:
            return x * y 
        elif x != None:
            return x * x 
        else:
            return 0
'''object'''
obj = Compute()
print('Area Value: ', obj.area())
print('Area Value: ', obj.area(4))
print('Area Value: ', obj.area(3, 5))



'''
# outputs
Area Value:  0
Area Value:  16
Area Value:  15
'''