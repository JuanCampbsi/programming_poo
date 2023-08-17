class Pessoa:
    def __init__(self, nome: str, endereco: str, telefone: str):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def apresenta_nome(self):
        return self.__nome


class PessoaFisica(Pessoa):
    def __init__(self, nome: str, endereco: str, telefone: str, cpf: int):
        self.__cpf = cpf
        super().__init__(nome, endereco, telefone)


class PessoaJuridica(Pessoa):
    def __init__(self, nome: str, endereco: str, telefone: str, cnpj: int):
        self.__cnpj = cnpj
        super().__init__(nome, endereco, telefone)

    def apresenta_nome(self):
        return f'{self.__cnpj} - {super().apresenta_nome()}'


pdf1 = PessoaFisica("Juan", "Rua lebretron", "99999-9999", 99999999999)
pdf2 = PessoaJuridica("Juan", "Rua lebretron", "99999-9999", 11111111111)

print(pdf1.apresenta_nome())
print(pdf2.apresenta_nome())
