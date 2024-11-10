#format specifiers -> {value:flags} format a value based on what flags are inserted


# :03       -> allocate and 0 pad that many spaces
# :<        -> left justify
# :>        -> right justify
# :^        -> center align
# :+        -> use a plus sign to indicate positive value
# :=        -> place sign to leftmost position
# :         -> insert a space before positive numbers
# :,        -> comma separator
price1 = 3.14159
price2 = -987.69
price3 = 12.34

#:.(number)f -> round to that many decimal places(fixed point)
print(f"price 1 is {price1:.2f}") #will print till 2 decimal place
print(f"price 2 is {price2:.3f}") #as there is no 3rd decimal it will print 0 as 3rd decimal

# :(number) -> allocate that many spaces
print(f"price 1 is {price1:10}") #as price1 takes 7 places so it will add 3 more space at the beginning
print(f"price 2 is {price2:8}") #as price1 takes 7 places so it will add 3 more space at the beginning









