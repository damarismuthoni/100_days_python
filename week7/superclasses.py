# base class 1
class Supermarket:
    #constructor
    def __init__(self, grocery, detergents, bakery):
        self.grocery = grocery
        self.detergent = detergents
        self.bakery = bakery

    # defining the methods
    def getGroceries(self):
        groc = input("Enter Grocery of Choice: ",)
        self.grocery = groc
        return self.grocery
    
list_1 = Supermarket("")
print(list_1.getGroceries())
    
    #method 2
    # def getDetergent(self):
        # deter = input("Enter your detergent of Choice: ",)