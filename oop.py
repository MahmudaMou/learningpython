#object = A bundle of related attributes(variables) and methods(functions).(When functions are used in object they are method)
#         Ex: phone,cup,book(A phone can have attribute like price,color etc. and method like call/massage)
#         you need a class to create many objects

#class->(blueprint) used to design the layout and structure of an object

#let's make class named Car
class Car:
    def __init__(self,model,year,color,for_sale):  #__init__ is constructor which is used here to construct object
        #these are attributes
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    #these are methods
    def drive(self):
        print(f"Please drive the {self.model}")
    def stop(self):
        print(f"Please stop the {self.model}")
    def description(self):
        print(f"{self.model} {self.color} {self.year} {self.for_sale}")


#while we create object all the self word is replaced by that object name in the backend

#now lets construct some car object(car1,car2 and car3 are the object of class car)
car1 = Car("Mustang",2025,"red",False)
car2 = Car("Corvette",2023,"blue",True)
car3 = Car("charger",2025,"yellow",True)

print(car1.color)
print(car2.year)
print(car3.model)
print(car1.for_sale)
car1.drive()
car2.stop()
car3.description()

#Class variables -> shared among all instance(means objects created from a class)
#                 class variables are define outside of constructor where instance variables
#                  are define inside of constructor
#                  class variable allow you to share data among all objects created from class where
#                  instance variable has their own version in every object

class Student:

    class_year = 2025 #this is a class variable
    num_student = 0

    def __init__(self,name,age):
        #these are instance variable
        self.name = name
        self.age =age
        Student.num_student +=1 # every time we will create a object num_student will increase by 1

student1 = Student("spongebob",30)
student2 = Student("Mahmuda",22)

#while accessing instance variable we call it by object name
print(student1.name)
#while accessing class variable it is good practice to call it by class name
print(Student.class_year)
print(Student.num_student)