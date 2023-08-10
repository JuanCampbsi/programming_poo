class Customer:
    __first_name = str
    __last_name = str
    __cpf_number = int
    __account = str

    def __init__(self, first_name: str, last_name: str, cpf_number: int):
        """

        Args:
            first_name:
            last_name:
            cpf_number:
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cpf_number = cpf_number
        self.__account = str

    def __str__(self) -> str:
        """

        Returns:
            str:
        """
        return f"Cliente: {self.__first_name} {self.__last_name}, CPF: {self.__cpf_number}\nBanco: {self.__account}"

    def link_account(self, account) -> object:
        """

        Returns:
            object:
        """
        self.__account = account
        return account

