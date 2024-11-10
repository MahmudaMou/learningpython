
#string
first_name = "Mou"
print(f"Hello {first_name}")

#intiger
age =20
print(f"My age is{age}")

#float
distance = 12.345
print(f"My distance is {distance}")

#boolean
new_student = ""
print(f"h{new_student}")
new_student = bool(new_student)
print(new_student)


is_student = False
if is_student:
    print("I am a student")
else:
    print("I am a teacher")

#typecasting (the process of convertinf a variable intp str() or int() float() bool())
name = "Mou"
age = 25
cgpa = 3.05
is_student = True
print(type(cgpa))
cgpa = int(cgpa)
print(type(cgpa))

#concat string
name += "s"
print(name)

#Taking input from the user
user_input  = input("Enter your name: ")
print(f"Hello {user_input}")

#when we take input by default it is string. We need to convert it before using
new_age = input("Enter your age: ")
new_age = int(new_age)
new_age += 1
print(f"My age is {new_age}")

#we can do this like this also
old_age = int(input("Enter your age: "))

#Exercise1->calculating the area
length = float(input("Enter your length: "))
width = float(input("Enter your width: "))
area = length * width
print(f"the area is {area} cm^2")




