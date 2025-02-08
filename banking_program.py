from random import choice


def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Please enter the amount you want to deposit: $"))
    if amount<0:
        print("This is nor a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Please enter the amount you want to withdraw: $"))
    if amount > balance:
        print("Insufficient Balance!")
        return 0
    elif amount < 0:
        print("This is nor a valid amount")
        return 0
    else:
        return amount


def main(): #it is a good practice to write the main block of code within the main() function
    is_running = True
    balance = 0
    while is_running:
        print("*******************")
        print("  Banking Program  ")
        print("1.Show Amount")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*******************")
        choice = input("Please Enter your choice(1-4)")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice!")
    print("Thank you for Banking with us!Good Bye!")


if __name__ == '__main__':
    main()