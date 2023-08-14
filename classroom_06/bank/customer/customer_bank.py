class Customer:
    __list_cliente = []

    def __init__(self, first_name: str, last_name: str, cpf_number: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cpf_number = cpf_number
        self.__account = str
        Customer.__list_cliente.append(self)

    @classmethod
    def search(cls, nome) -> str:
        search_name = ""
        for cliente in cls.__list_cliente:
            if cliente.__first_name == nome:
                search_name = cliente.__first_name
                return search_name
            else:
                return "Nome não encontrado"

    @staticmethod
    def operating(value) -> str:
        return f"Teste  método estático: {value}"



