class Customer:
    def __init__(self, first_name, last_name, social_security_number):
        self.first_name = first_name
        self.last_name = last_name
        self.social_security_number = social_security_number
        self.account = None  # Initially, the customer doesn't have an account linked yet

    def link_account(self, account):
        self.account = account  # link the account to the customer


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
