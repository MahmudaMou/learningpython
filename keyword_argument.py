#keyword arguments-> an argument preceded(come before) by an identifier
#                    these arguments helps with readability
#                    order of argument doesn't matter
def hello(greeting,title,first_name,last_name):
    print(f"{greeting} {title} {first_name} {last_name}")

hello("Hello",title="Mis",first_name="Mahmuda",last_name="Khanam") #when you mix keyword argument with non
#                                                              keyword argument the position of non-key should maintain
#a lot of built in function has keyword arguments that we use.Here is an example
for x in range(1,10):
    print(x,end=" ") #In the print function call end="" is a keyword argument
print()
#another example
print("1","2","3","4",sep="-") #here sep="-" is an keyword argument

