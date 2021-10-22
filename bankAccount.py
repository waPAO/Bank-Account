class BankAccount:
    # Initialize object
    def __init__(self, full_name: str, accountNumber: int, balance = 0) -> None:
        self.name = full_name
        self.number = accountNumber
        self.balance = balance
    
    # Deposit money that will be added into balance
    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${'%.2f'%self.balance}")
    
    # Withdraw money that will be deducted from balance
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insufficient funds")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance: ${'%.2f'%self.balance}")

    # Returns balance and prints out balance
    def get_balance(self) -> float:
        print(f"Current Account Balance: ${'%.2f'%self.balance}")
        return self.balance
    
    # Add interest to balance
    def add_interest(self) -> None:
        interest = self.balance * 0.00083
        self.balance += interest
    
    # Print account details
    def print_statement(self) -> None:
        print(f"{self.name}\nAccount No.: ****{str(self.number)[-4:]}\nBalance: ${'%.2f'%self.balance}")

# Tests
if __name__ == "__main__":
    pass