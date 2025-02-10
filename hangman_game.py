import random
import word_list
words = word_list.words
#Now we will make a dictionary of ke:(value)
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " | ",
                   "   "),
               3: (" O ",
                   "/| ",
                   "   "),
               4: (" O ",
                   "/|\\",
                   "   "),
               5: (" O ",
                   "/|\\",
                   "/ "),
               6: (" O ",
                   "/|\\",
                   "/ \\")
               }

def display_man(wrong_guess):
    print("************")
    for latter in hangman_art[wrong_guess]:
        print(latter)
    print("************")

def display_hints(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letters = set()
    is_playing = True
    while is_playing:
        display_man(wrong_guess)
        display_hints(hint)
        guess = input("Enter a letter: ").lower()
        if len(guess) !=1 or not guess.isalpha():
            print("Invalid guess")

        if guess in guessed_letters:
            print(f"{guess} is already guessed")

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1

        if "_" not in hint:
            display_man(wrong_guess)
            print("You Win!")
            display_answer(answer)
            is_playing = False
        elif wrong_guess >= len(hangman_art) -1:
            display_man(wrong_guess)
            display_answer(answer)
            print("You Lose!")
            is_playing = False

if __name__ == '__main__':
    main()

