# Pets example with Pirple.com
print("Pirple.com - Classes and Class Inheritance")


class Pet:
    def __init__(self, n, a, h, p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p

    # getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

    # setters
    def setName(self, newName):
        self.name = newName
        return

    def setAge(self, newAge):
        self.age = newAge
        return

    def setHunger(self, newHunger):
        self.hunger = newHunger
        return

    def setPlayful(self, newPlayful: bool) -> object:
        self.playful = newPlayful
        return

pet1 = Pet("Dave", 3, False, True)
print(pet1.getName())
pet1.setName("Steve")
print(pet1.getName())