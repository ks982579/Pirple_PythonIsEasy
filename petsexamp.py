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
# End Pet Class

class Dog(Pet):
    def __init__(self, dName, dAge, dHunger, dPlayful, breed, favToy):
        Pet.__init__(self, dName, dAge, dHunger, dPlayful)
        self.breed = breed
        self.favouriteToy = favToy

Johny = Dog("Johny", 4, False, False, "unknown", "stick")
print(Johny.getAge())

class Cat(Pet):
    def __init__(self, cName, cAge, cHunger, cPlayful, cSleeping):
        Pet.__init__(self,cName,cAge,cHunger,cPlayful)
        self.sleeping = cSleeping
    def isAsleep(self):
        if(self.sleeping):
            msg = self.name+" is sleeping."
        else:
            msg = self.name+" is awake."
        return msg
Jerry = Cat("Jerry", 3, True, True, False)
print(Jerry.isAsleep())

class Human:
    def __init__(self,name: str,pets: list = []):
        self.name = name
        self.pets = pets

    def hasPets(self):
        if(len(self.pets)>0):
            return "yes"
        else:
            return "no"
# End Human Class

YourSelf = Human("Bruce", [Johny, Jerry])
print(YourSelf.hasPets())