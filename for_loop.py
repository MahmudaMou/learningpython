#following code will count 1 to 10
for x in range(1,11):
    print(x)
print("Happy New Year") #this line will be out of for loop
#if we don't specify the first range it will start counting from 0
print("without specifing the first range")
for x in range(11):
    print(x)
#following code will count 10 to 1. the third number in the range function(2) is the step.
for x in reversed(range(1,11,2)):
    print(x)
#following is another way of reversing
print("another way of reversing")
for x in range(11,0,-1):
    print(x)


#you can loop through a string
print("Loop through string")
credit_card = "1234-5678-9827"
for x in credit_card:
    print(x)
# let's say wile counting 1 to 10 we want to skip 7
print("skip 7")
for x in range(1,11):
    if x == 7:
        continue
    else:
        print(x)



