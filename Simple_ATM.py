class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Successfully deposited ${amount}. Your new balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. Your new balance is: ${self.balance}")

#main function
def main():
    atm = ATM()

    while True:
        print("\n==== ATM Menu ====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
