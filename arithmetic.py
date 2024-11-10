# augmented assignment operator
from math import remainder

friends = 0
# friends = friends +1
friends += 1
# friends = friends -2
friends -= 2
# friends = friends * 3
friends *= 3
# friends = friends/3
friends /= 3
friends = 5
# exponent means to the power
# friends = friends ** 3 means friends to the power 3
friends **= 2
# remainder = friends % 3
print(friends)

# functions
x = 3.14
y = -5
z = 6
# round function rounds float to nearest integer
result = round(x)
# abs() function gives the absolute value which is the distance away from 0 as a whole number
results = abs(y)
# print(results)
# we can do exponents with pow function
power = pow(2, 3)
# print(power)
maxValue = max(x, y, z)
print(maxValue)
# for math. function I have to import math
import math

R = 9.9
# this will print the value of pi
# print(math.pi)
# this will print the value of e
# print(math.e)
# square root of x
# sqroot = math.sqrt(R)
# print(sqroot)
# ceil will give the next round number
# print(math.ceil(R))
# floor will just cut off the doshomik
# print(math.floor(R))

# Exercise
# calculate the circumference of a circle
radius = float(input("Enter radius: "))
circumference = 2 * math.pi * radius * radius
print(circumference)







