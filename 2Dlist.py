fruits = ["apple","orange","banana","coconut","pineapple"]
birds = ["parrot","crow","pigeon","moyna","owl"]
animals = ["tiger","deer","lion","cat","dog"]

zoo=[fruits,birds,animals] #it is a 2D list.

#in 2D list every item is a row.so zoo[0] is the first row
print(zoo[0])
#to access a specific element we have to specify both the row and column
#for example: to access crow-> as it is in row 1 and column 1
print(zoo[1][1])

#2d list can also be written like this
zoo = [["apple","orange","banana","coconut","pineapple"],
       ["parrot","crow","pigeon","moyna","owl"],
       ["tiger","deer","lion","cat","dog"]]
#to iterate through a 2d list we need nested loop
for collection in zoo:
    for item in collection:
        print(item, end=" ")
    print()
#Like this we can make 2d tuple or set.
#also a 2d tuple with 1d sets or 1d lists or either way whatever is best useful

#-----------------Example1->2D typepad-------
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for nums in num_pad:
    for num in nums:
        print(num, end=" ")
    print()



