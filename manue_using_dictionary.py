#concession(a contract granting the right to operate a subsidiary business)
#concession standing(a place where food, drinks, and sometimes merchandise are sold at a public venue) program
menu = {"pizza": 3.00,
        "nachos":4.50,
        "popcorn":6.00,
        "fries":2.3,
        "chips":3.33,
        "pretzel":4.5,
        "soda":3.00,
        "lemonade":3.5}
cart = []
total = 0
print("----------- MENU----------- ")
for key,value in menu.items():
    print({f"{key:10}: ${value:.2f}"})
print("--------------------------- ")

while True:
    food = input("select an item(q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------- Your Order ----------- ")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: ${total:.2f}")
