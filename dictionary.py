# dictionary consists of a collection of {key:value} pairs
#             these collections are ordered and changeable
#             also duplicates are not allowed in these collections

capitals = {"USA": "Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}
#Here capitals is a dictionary.IT is a collection where counties are the keys and capitals are the values
#Just a reminder->as dictionaries are collections we can use dir() and help() function to know all available
#                                 attributes and methods
#print(dir(capitals))
#print(help(capitals))

print(capitals.get("USA")) #thise will print the value associated with the key
print(capitals.get("Japan")) #as Japan is not in the dictionary it will return none as it's not in the dictionary

if capitals.get("japan"):
    print("exist")
else:
    print("doesn't exist")

capitals.update({"Germany":"Berlin"}) #this will add new item at the end
print(capitals)
capitals.update({"USA":"Detroit"}) #this will update the value of key usa
print(capitals)
capitals.pop("China") #this will remove china
print(capitals)
capitals.popitem() #this will remove the last item
print(capitals)
#capitals.clear() #this will remove all the item and empty the dictionary
#print(capitals)

#keys() method will return all the keys of dictionary as object of list
keys = capitals.keys()
print(keys)

#as it returns the keys as objects,these are iterable.we can iterate in for loop
for key in keys:
    print(key)

#values() method will return all the values of dictionary as object of list
values = capitals.values()
print(values)

#as it returns the keys as objects,these are iterable.we can iterate in for loop
for value in values:
    print(value)

#item() -> it returns a dictionary object which resembles a 2d list of tuples
#            item -> [(),(),()]
items = capitals.items()
print(items)
for key,value in capitals.items():
    print(f"{key}:{value}")

#Exercise
grades={"Sandy":"A",
        "Anita":"C",
        "Mohit":"B",
        "Bhumi":"A"}
student = input("Enter Student Name: ")
if student in grades:
    print(f"{student}'s grad is {grades[student]}")
else:
    print("Student not found")
    





