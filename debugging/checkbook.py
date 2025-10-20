class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            print("Exiting the checkbook program. Goodbye!")
            break
        
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount cannot be negative. Please enter a positive number.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for deposit.")
        
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount cannot be negative. Please enter a positive number.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for withdrawal.")
        
        elif action == 'balance':
            cb.get_balance()
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
