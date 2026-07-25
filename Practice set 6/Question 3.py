class Animal:
    def sound(self):
        print("Some Sound")

class Dog(Animal):
    def sound(self):
        print("Barks!")

obj = Dog()
obj.sound()
