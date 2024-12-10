age = int(input("Enter your age: "))
#while loop is infinite.once the condition is true it will run infinite time
#while age<0:
#    print("age cant be negative")
#this will run infinite time.to stop this we will need a escape statement
#------Example-1-------------
while age<0:
    print("age cant be negative")
    age = int(input("please enter a valied age: ")) #this is the escape statement
print(f"you are {age} years old")
#------Example-2-------------
name = input("Enter name:")
while name=="":
    print("you have not enter your name") #this line will continue infinite
    name = input("Please enter name: ") #this is the escape statement
print(f"hello {name}")
#------Example-3-------------
food = input("Enter your favourite food (or type q to quite): ")
while not food == "q":
    print(f"your favourite food is {food}") #this will continue infinite
    food = input("Enter another food (or type q to quite): ") #this is the escape statement
print("ok bye")
#------Example-4-------------
num = int(input("Enter a number between 1-10: "))
while num<0 or num>10:
    print("the number is not between 1-10")
    num = int(input("Please enter a number between 1-10: "))
print(f"the number is {num}")




