class Item:
    def __init__(self,name,price,qty):
        self.name = name
        self.price = price
        self.qty = qty
    def purchase(self,qty):
        if self.qty>=qty:
            self.qty-=qty
            print('purchasing done....')
        else:
            print('out of stock')
    def increaseStock(self,qty):
        self.qty+=qty
        print('quantity updated....')
    def display(self):
        print('\nName of product:',self.name)
        print('Price per unit:',self.price)
        print('Quantity of products:',self.qty)

obj1=Item('apple',30,100)
obj2=Item('orange',20,150)

obj1.purchase(5)
obj1.purchase(200)
obj1.increaseStock(10)
obj1.display()

obj2.display()