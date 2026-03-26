#bank program

def show_balance(balance):
    print(f"The banalce is {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit : "))

    if amount < 0:
        print("Thats not a valid amount")
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw : "))

    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:

        print("**** Bank program ****")
        print("1.Show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")

        choice = input("Enter the choice(1,2,3,4) : ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("This is not a valid choice")

    print("thank you have a nice day")

if __name__ == "__main__":
    main()