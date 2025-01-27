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
#There are 4 types of argument->1.Positional,2.Default,3.keyword 4.arbitrary
#1.positional
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

#2.Default argument-> A default value for certain parameter
#                   Default is used when the e is omitted
#Remember! you have to write the default value argument after the non default argument
def net_price(list_price,discount=0,tax=0.05): #Here discount and tax has default value
    return list_price*(1-discount)*(1+tax)
print(net_price(500))  #here we don't have to pass discount or tax as they have default value
#But if we want to pass different value we can just pass it
print(net_price(500,0.1,0))

#stopwatch project
import time
def count(end,start=0): #as we have to write default valued argument after so we wrote start 2ed
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")
count(10)