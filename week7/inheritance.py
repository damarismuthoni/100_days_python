# case study 1 on inheritance
class person:

#creating gthe constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
#now creating methods
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
#Derived class 1 on education
class education(person):

#method1 in the derived class education
    def isEducated(self):
        return True
person_1 = person("Hailey", 23)
person_1 = education("Hailey", 23)

#print statements
print(person_1.isEducated())
print(person_1.getName())