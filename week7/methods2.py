class Animals:
    def __init__(self, name, sound, type ):
        self.name = name
        self.sound = sound
        self.type = type 

    def getName(self):
        return self.name
    def getSound(self):
        return self.sound 
    def getType(self):
        return(self.type)

Animals_1 = Animals("Lion", "Roars", "Mammal" )
print(Animals_1.getName())
print(Animals_1.getSound())
print(Animals_1.getType())