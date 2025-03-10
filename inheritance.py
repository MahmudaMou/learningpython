#Inheritance  -> allows a class to inherit attributes and methods from another class
#                Helps with code reusability and extensibility
#                class child(parent)

#we will create parent class Animal and child class dog at and mouse

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):   #to inherit we have to write the names(can be more than 1) of parent class inside ()
    def speak(self): #along with all attributes ans methods of their parent class they can have their own
        print("WOOF!")
class Cat(Animal):
    pass
class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Micky")

#Even though we have nothing in the cat doh and mouse class we still everything of animal class

print(dog.name)
print(dog.is_alive)
cat.eat()
mouse.sleep()