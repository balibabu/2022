x = -5
def display(x):
    print(x)    #this x is global
    x = 5  #local variable is valid inside function only
    print(x) #this x is local
display(x)
print(x)
