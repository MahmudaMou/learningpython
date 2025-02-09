import random
def spin_row():
    spins = ['🍒','🍉','🍋','🔔','⭐']
    lists = []
    [lists.append(random.choice(spins)) for _ in range(3)]
    return lists

def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet*3
        elif row[0] == '🍉':
            return bet*4
        elif row[0] == '🍋':
            return bet*5
        elif row[0] == '🔔':
            return bet*10
        elif row[0] == '⭐':
            return bet*20
    else:
        return 0


def main():
    balance =100

    print("***********************")
    print("    Welcome to slots   ")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐")
    print("***********************")
    print(f"Your current balance is ${balance}")
    while balance>0:
        bet = input("Enter your bet: $")
        if not bet.isdigit():
            print("Invalid amount")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance")
            continue
        if bet<=0:
            print("Bet must be greater than 0!")
            continue
        balance -= bet
        print("Spinning.......")
        row = spin_row()
        print_row(row)
        payout = get_payout(row,bet)
        if payout>0:
            print(f"Congratulations!you won ${payout}")
        else:
            print("Sorry!You lose this round")
        balance += payout
        print(f"Your balance is  ${balance}")
        play_again = input("Do you want to play again(Y/N):").upper()
        if play_again == 'Y':
            continue
        else:
            break
    print(f"Game Over!Your Final balance is ${balance}")


if __name__ == '__main__':
    main()
