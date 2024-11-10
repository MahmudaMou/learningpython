#indexing -> [start : end : step]
credit_number = "123-456-789-123"
print(credit_number[3]) #this will print the character at index 3
print(credit_number[0:4:2]) #this will print from index 0 to index 4 and stepping 2
print(credit_number[0:4]) #this will print from index 0 to index 4 and by default stepping 1
print(credit_number[:4]) #this will also print from 0 to 4
print(credit_number[4:]) #this will from 4 to end
print(credit_number[-1]) #negative number will count the index from the end.so it print last number
print(credit_number[::3])#this will print from start to end stepping 3

#--------------Exercise-1-----
#print the last digit of the credit card number
last_digit = credit_number[-4:]
print(f"XXX-XXX-XXX{last_digit}")
#----------Exercise-2-----------
#reverse the credit card number
reverse_number = credit_number[::-1]
print(reverse_number)


