class Person:
    # we begin by uilding the constructor
    def __init__(self, name, age) :
        self.name = name
        self.age = age 

    # next we create a method getName 
    def getName (self):
        return self.name
    
person1 = Person("Alice", 30)
name = person1.getName()
print(name)