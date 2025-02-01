#list comprehension-> A concise(giving a lot of information clearly and in a few words) way to create loop in python
#                      compact and easier to read than traditional loops
#                      structure-> [expression For Value in iterable if condition]

#Traditional way to make list of double
doubles =[]
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

#in list comprehension way->
double_list = [x*2 for x in range(1,11)]
print(double_list)

fruits = ["apple","banana","mango","litchi"]
fruits =[x.upper() for x in fruits]
print(fruits)
fruits_chars =[fruit[0] for fruit in fruits]
print(fruits_chars)

numbers = [1,-1,2,-2,0,3,4,-4,5]
positive_nums = [num for num in numbers if num>=0] #as we don't have any expression here we simply return num
even_numbers = [num for num in numbers if num%2==0]
odd_numbers = [num for num in numbers if num%2==1]

print(odd_numbers)