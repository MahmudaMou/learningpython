# collection = single variable used to store multiple values
#   List  = []  ordered and changeable. Duplicates OK
#   set   = {}  unordered and immutable, but Add/Remove OK.No Duplicates
#   Tuple = ()  ordered and unchangeable. Duplicates Ok .FASTER

#------------------LIST-----------------------------------------
fruits = ["apple","orange","banana","coconut","pineapple"]
print(fruits) #this will print the entire list
print(fruits[2]) #this will print the fruit at index 2
print(fruits[0:2]) #this will print the fruit from 0 index to 2 index

#another way of printing the list
for x in fruits:
    print(x)

print(len(fruits)) #will print the length of collection
print("apple" in fruits) #print weather apple is in fruits collection
fruits[0] = "cucumber" #this will change the first value from apple to cucumber
fruits.append("tomato") #this will add tomato at the end
fruits.remove("banana") #this will remove banana
fruits.insert(3,"potato") #this will add potato at index 3
fruits.sort() #this will sort the list alphabetically
fruits.reverse() #this will reverse
print(fruits.index("potato")) #the index of given item
print(fruits.count("potato")) #as there can be duplicate this will count them
#fruits.clear() #this will empty the list

print(fruits)

#---------------------------------SETS-----------------------------------------
#   set   = {}  unordered and immutable(means we can't alter these values), but Add/Remove OK.No Duplicates
birds = {"parrot","crow","pigeon","moyna","owl"}
print(birds) #as it is not ordered items will print randomly
#print(birds[0]) #this will give error as sets are unordered so indexing is not possible
birds.add("sparrow")
birds.remove("crow")
birds.add("parrot") #as duplicates are not allowed there will be only one parrot.
birds.pop() #it will randomly remove an item
print(birds)
#------------------------------------Tuple----------------------------------------
#   Tuple = ()  ordered and unchangeable. Duplicates Ok .FASTER
animals = ("tiger","deer","lion","cat","dog")


#you can iterate all the collection
for fruit in fruits:
    print(fruit)


#to know all the function available in collections
#print(dir(fruits))   #this will print all the available function for that collection
#print(help(fruits))   #this will print all the available methods and their descriptions