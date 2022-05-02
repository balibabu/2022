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

def controller(item):
    print('\n1.Exit\n2.Purchase\n3.Increase Stock\n4.Display')
    while True:
        choice=int(input('enter your choice:'))
        if choice==1:
            break
        elif choice==2:
            qty=int(input('enter quantity:'))
            item.purchase(qty)
        elif choice==3:
            qty = int(input('enter quantity:'))
            item.increaseStock(qty)
        elif choice==4:
            item.display()
        else:
            print('invalid choice')

def main():
    items={}
    print('1.Exit\n2.Add new Item\n3.Manage old item\n4.Display all items')
    while True:
        choice = int(input('enter your choice:'))
        if choice == 1:
            break
        elif choice == 2:
            name=input('enter name of product:')
            qty = int(input('enter quantity:'))
            price=int(input('enter price per item:'))
            try:
                items[name]=Item(name,price,qty)
            except:
                print('Item already exists')
        elif choice == 3:
            try:
                controller(items[input('enter name of product:')])
                print('\n\n1.Exit\n2.Add new Item\n3.Manage old item\n4.Display all items')
            except:
                print('Item not found')
        elif choice == 4:
            print('List of items in the shop:')
            for i in items:
                print(i)
            else:
                print('no items')
        else:
            print('invalid choice')

if __name__ == '__main__':
    main()