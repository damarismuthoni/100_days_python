class electric_shop:
    def __init__(self, pd_name, quantity, price):
        self.name = pd_name
        self.quantity = quantity
        self.price = price

# now we create a derived class that will hold the methods 

class methods(electric_shop):

    #defining method one within the methods class which inherits from electric shop

    def getName(self):
        return self.name
    
    def getQuantity(self):
        quantity = int(input("Enter Quantity of Items: ",))
        self.quantity = quantity
        return self.quantity
    
    def getprice(self):
        cost = int(input("Enter cost of Item:",))
        self.price = self.quantity * cost
        return self.price
    
    #object methods

laptop = methods("Asus", 0, 0)
# print(laptop.getQuantity())

checkout_price = electric_shop("Lenovo", 0, 0)
print("You have " + str(laptop.getQuantity()) + " items in your Cart"  )
print("That will cost you " + str(laptop.getprice() ))
