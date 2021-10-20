class BankAccount:
    def __init__(self, full_name: str, account_number: int, balance = 0) -> None:
        self.name = full_name
        self.number = account_number
        self.balance = balance
        
    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")
    
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insufficient funds")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance: ${self.balance}")

    def get_balance(self) -> float:
        print(f"Current Account Balance: ${self.balance}")
        return self.balance
    
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest