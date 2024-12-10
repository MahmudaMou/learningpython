#format specifiers -> {value:flags} format a value based on what flags are inserted
price1 = 3.14159
price2 = -987.69
price3 = 12.34

#:.(number)f -> round to that many decimal places(fixed point)
print(f"price 1 is {price1:.2f}") #will print till 2 decimal place
print(f"price 2 is {price2:.3f}") #as there is no 3rd decimal it will print 0 as 3rd decimal

# :(number) -> allocate that many spaces
print(f"price 1 is {price1:10}") #as price1 takes 7 places so it will add 3 more space at the beginning
print(f"price 2 is {price2:8}") #as price2 takes 7 places so it will add 1 more space at the beginning

# :03       -> allocate and 0 pad that many spaces
print(f"price 1 is {price1:010}") #as price1 takes 7 places so it will add 3 0 instead of space at the beginning

# :<        -> left justify
# :>        -> right justify
print(f"price 1 is {price1:<10}")
print(f"price 2 is {price2:>8}")

# :^        -> center align
print(f"centered aligned price 1 is {price1:^2}")

# :+        -> use a plus sign to indicate positive value.
print(f"signed price 1 is {price1:+}")
print(f"signed price 2 is {price2:+}") #+ sign will not appear as it is a negative value


print(f"all price 1 is {price1:+,.2f}")
print(f"all price 2 is {price2:+,.2f}")

#some others
# :=        -> place sign to leftmost position
# :         -> insert a space before positive numbers
# :,        -> comma separator


















