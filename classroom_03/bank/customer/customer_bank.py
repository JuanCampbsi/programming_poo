class Customer:
    def __init__(self, first_name: str, last_name: str, cpf_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf_number = cpf_number
        self.account = str

    def __str__(self):
        return f"Cliente: {self.first_name} {self.last_name}, CPF: {self.cpf_number}\nBanco: {self.account}"

    def link_account(self, account):
        self.account = account

