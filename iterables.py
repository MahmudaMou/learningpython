#Iterables->An object/collection that can return its elements one at a time
#           allowing it to iterate over in a loop
#            lists[] sets{} and tuples() are iterable
numbers_list = ["1","2","3"]
for number in reversed(numbers_list):
    print(number)
numbers_tuples = ("1","2","3")
for number in reversed(numbers_tuples):
    print(number)
numbers_set = {"1","2","3"}
for number in numbers_set:   #we can't use reversed method here as sets are immutable
    print(number)


