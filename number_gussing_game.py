import random
lowest_num =1
height_num =100
answer = random.randint(lowest_num,height_num)
guesses =0
is_running = True
print("Python number guessing game")
print(f"select a number between {lowest_num} to {height_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if lowest_num > guess or  guess> height_num:
            print("The number is out of the range")
            print(f"Please select a number between {lowest_num} to {height_num}")
        elif guess < answer:
            print("Too low!Try again!")
        elif guess > answer:
            print("Too high!Try again!")
        else:
            print(f"CORRECT!The answer was {answer}")
            print(f"Number of guesses {guesses}")
            is_running = False
    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowest_num} to {height_num}")

