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