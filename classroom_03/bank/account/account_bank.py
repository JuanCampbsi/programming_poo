class BankAccount:
    __number = int
    __branch = str
    __balance = int
    __customer = str

    def __init__(self, number: int, branch: str, balance=0):
        """

        Args:
            number:
            branch:
            balance:
        """
        self.__number = number
        self.__branch = branch
        self.__balance = balance
        self.__customer = str

    def __str__(self) -> str:
        """

        Returns:
            str:
        """
        return f"Conta {self.__number} - Agência {self.__branch} - Saldo {self.__balance}"

    def link_customer(self, customer) -> object:
        """

        Args:
            customer: 

        Returns:
            object:
        """
        self.__customer = customer
        return customer.link_account(self)

    def deposit(self, amount) -> int:
        """

        Args:
            amount:

        Returns:
            int:
        """
        if amount > 0:
            self.__balance += amount
        return amount

    def withdraw(self, amount) -> int:
        """

        Args:
            amount:

        Returns:
            int:
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return amount
