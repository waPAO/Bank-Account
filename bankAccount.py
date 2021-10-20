class BankAccount:
    def __init__(self, full_name: str, account_number: int, balance = 0) -> None:
        self.name = full_name
        self.number = account_number
        self.balance = balance
        