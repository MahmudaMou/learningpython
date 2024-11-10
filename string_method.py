name = input("Enter your full name:")
length_of_name = len(name)
#it counts length of string with space
print(f"length of name is {length_of_name}")
search_character = name.find("o")
#this will return the position of the first o in the name
print(f"position of first o is {search_character}")
search_last = name.rfind("o")
#r means reverse.It will search from end and return the position of last o
print(f"position of last o {search_last}")
capital_first_word = name.capitalize()
#it will make only the first word capital
print(capital_first_word)
upper_case = name.upper()
#it will make all the word upper case
print(upper_case)
check_digit= name.isdigit()
#it will be true only of all the words are digit
print(f"is there only digit in name {check_digit}")
check_alphabet = name.isalpha()
#it will check if there is only alphabet.a space is not counted as alphabet
print(f"is there only alphabet in name {check_alphabet}")
count_letter = name.count("o")
print(count_letter)
replace_letter = name.replace("o","t")
print(replace_letter)
#to get the list of all available string methods
#print(help(str))

#--------------Exercise-1----------
#validate user input
#username is no more than 12 character
#username must not contain space
#username must not contain digit
username = input("Enter your username: ")
if len(username) > 12:
    print("username can not be more than 12 character")
elif not username.find(" ") == -1:
    print("username can not contain space")
elif not username.isdigit():
    print("username can not contain digit")
else:
    print(f"welcome {username}!")





