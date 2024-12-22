class Animal:

    def __init__(self,Habitat):
        self.habitat=Habitat

    def printHabitat(self):
        print(self.habitat)

    def sound(self):
        print("some animal sound")


class Dog(Animal):

    def sound(self):
        print("wook woof")

ob=Dog("Jungle")
ob.printHabitat()
ob.sound()
