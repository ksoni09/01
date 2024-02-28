class BankAccount:
    def __init__(self, account_number, holder_name, account_type):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"Deposited ${amount} successfully.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount} successfully.")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def get_account_type(self):
        return self.account_type

    def get_account_number(self):
        return self.account_number

    def get_holder_name(self):
        return self.holder_name

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

# Test the BankAccount class
def main():
    # Create a bank account
    account1 = BankAccount("1234567890", "John Doe", "Savings")

    # Deposit money
    account1.deposit(1000)

    # Withdraw money
    account1.withdraw(500)

    # Check balance
    account1.check_balance()

    # Display account details
    print("Account Number:", account1.get_account_number())
    print("Account Holder Name:", account1.get_holder_name())
    print("Account Type:", account1.get_account_type())

    # Display transaction history
    account1.display_transaction_history()

if __name__ == "__main__":
    main()