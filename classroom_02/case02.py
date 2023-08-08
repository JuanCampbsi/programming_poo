class Customer:
    def __init__(self, first_name, last_name, cpf_number):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf_number = cpf_number
        self.account = None

    def link_account(self, account):
        self.account = account


class BankAccount:
    def __init__(self, number, branch, balance=0):
        self.number = number
        self.branch = branch
        self.balance = balance
        self.customer = None

    def link_customer(self, customer):
        self.customer = customer
        customer.link_account(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
