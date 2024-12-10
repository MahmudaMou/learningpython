foods = [] #we are not using tuple as tuple is unchangeable.not using sets as sets are unordered
prices = []
total = 0
while True:
    food = input("Enter a food to buy(q to quit): ")
    if food.lower() == "q": #used lower() to lowercase in case user type Q
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("--------Your Shopping card---------")
for food in foods:
    print(food, end=" ")
for price in prices:
    total += price
print()
print(f"your total is ${total}")
