# function = A block of reusable code
#            place () after the function name to invoke it
# in python to make a function write def then function name then () and at last :
def hello_world():
    print("Hello")
    print("This is my First Function!")
#and now to call it just write function_name()
hello_world()
hello_world()

#passing argument is like php
def happy_birthday(name,age):
    print(f"Happy Birthday {name}")
    print(f"you are {age} years old!")
happy_birthday("Mou",20)
happy_birthday("Avi",30)

#return ->statement used to end a function and send a result back to a caller
def add(x,y):
    z = x+y
    return z
def subtract(x,y):
    z = x-y
    return z
def multiply(x,y):
    z = x*y
    return z
def divide(x,y):
    z = x/y
    return z
print(add(2,3))
print(subtract(5,2))
print(multiply(2,3))
print(divide(6,3))

def create_name(first,last):
    first =first.capitalize()
    last = last.capitalize()
    return first+" "+last
print(create_name("mahmuda","khanam"))