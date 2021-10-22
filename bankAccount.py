from random import randint

class BankAccount:
    # Initialize object
    def __init__(self, full_name: str, type = "checking") -> None:
        self.name = full_name
        self.number = randint(10000000, 99999999)
        self.balance = 0
        if type == "checking":
            self.type = type
        elif type == "savings":
            self.type = type
        else:
            print("Bank account type does not exist, please input 'checking' or 'savings'")
    
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
        if self.type == "checking":
            interest = self.balance * 0.00083
            self.balance -= interest
        else:
            interest = self.balance * 0.001
            self.balance -= interest
    
    # Print account details
    def print_statement(self) -> None:
        print(f"{self.name}\nAccount No.: ****{str(self.number)[-4:]}\nBalance: ${'%.2f'%self.balance}")

# Tests
if __name__ == "__main__":
    Pao = BankAccount("Pao Lo", "savings")
    Nik = BankAccount("Nik Oh", "checking")
    Shwa = BankAccount("Shwa Bae")
    Pao.deposit(33.55)
    Nik.deposit(9.05)
    Shwa.deposit(12)
    print()
    Pao.print_statement()
    Nik.print_statement()
    Shwa.print_statement()
    Pao.add_interest()
    Nik.add_interest()
    Shwa.add_interest()
    print()
    Pao.print_statement()
    Nik.print_statement()
    Shwa.print_statement()
    Nik.withdraw(10)
    Shwa.withdraw(10)
    print()
    Pao.print_statement()
    Nik.print_statement()
    Shwa.print_statement()
    # Mitchell Testing
    print()
    Mitchell = BankAccount("Mitchell")
    Mitchell.deposit(400000)
    Mitchell.print_statement()
    Mitchell.add_interest()
    Mitchell.print_statement()
    Mitchell.withdraw(150)
    Mitchell.print_statement()