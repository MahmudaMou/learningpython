# *args means argument->allows you to pass multiple non key arguments
# **kwargs means keyword arguments->allows you to pass multiple  key-arguments
#when you invoke a function with *args/**kwargs as parameter you can pass variable number of arguments
# and the arguments will pac into a tuple(if it is *args) or dictionary(if it is a **kwargs)
#Remember-> here * and ** are operator.you can use nay name.Means *number will work same as *args

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3,4))
#another example
def display_name(*names):
    for name in names:
        print(name,end=" ")
display_name("Mrs","Mahmuda","Khanam","Mou")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_address(street="123 fake street",
              apt="100",
              city="Detroit",
              state="MI",
              Zip="54321")
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=",")
    if "country" in kwargs:
        print(f"{kwargs.get('country')}") #here used single quot otherwise python will get confused with too many double quot


shipping_label("Mr","SpongeBob","Square pants","II",  #as in function *args are writen first here *args should be first
               street="123 fake street",
               apt="100",
               city="Detroit",
               state="MI",
               Zip="54321",
               country="Bangladesh"
               )