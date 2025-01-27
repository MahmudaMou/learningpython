import random
#print(help(random)) #to know all available methods
#***Remember you can not use random word as variable name in random module***

number = random.randint(1,20) #this will give a random integer from 1 to 20
print(number)
low = 0
high = 100
guess = random.randint(low,high)
print(guess)

float_number = random.random() #this will return a random floating point number from 0 to 1
print(float_number)

options = ("rock","paper","scissors") #the choice method will choose a option
option = random.choice(options)
print(option)

#shuffle() method will shuffle the items
cards =["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)