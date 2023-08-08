class BankAccount:
    def __init__(self, number: int, branch: str, balance=0):
        self.number = number
        self.branch = branch
        self.balance = balance
        self.customer = str

    def __str__(self):
        return f"Conta {self.number} - Agência {self.branch} - Saldo {self.balance}"

    def link_customer(self, customer):
        self.customer = customer
        customer.link_account(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
