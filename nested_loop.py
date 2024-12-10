#nested loop = a loop inside another loop.
for x in range(3):
   for y in range(1,10):
     print(y, end="") #, end="" this will print all number in one line. , end="-" will add - between them
   print() #this will give outer loop a new line

#---------create a rectangle-----------
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to create the rectangle: ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()

