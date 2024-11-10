#age = int(input("Enter your age: "))
age = 12
if age >= 18:
    print("You are registered")
elif age < 0:
    print("You are not born yet")
else:
    print("You are not registered")


#with boolean
online = True
if online:
    print("You are online")
else:
    print("You are not online")

#with string
#response = input("Would you like food?(Y/N)")
response = "Y"
if response == "Y":
    print("Have some food")
else:
    print("Thank you")

#logical operator
#or -> either
#and -> both
#not -> inverts the condition(not False, not true)

temp =40
is_raining = False

if temp>30 or temp < 0 or is_raining:
    print("outdoor is cancelled")
else:
    print("outdoor is still scheduled")

is_sunny = False

if temp >33 and not is_sunny:
    print("it is very hot and cloudy outside")
elif temp<20 and is_sunny:
    print("it is cold and sunny outside")
else:
    print("temperature is ok")

#conditional expression:-> A one line shortcut for if-else statement

num = -5
print("positive" if num >0 else "negative")
result = ("EVEN" if num % 2 == 0 else "ODD")
print(result)

a=6
b=5
max_num = a if a>b else b
min_num = b if b<a else a
print(max_num ,min_num)


