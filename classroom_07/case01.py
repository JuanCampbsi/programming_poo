class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int):
        self.__portas = portas
        super().__init__(marca, modelo)

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, portas):
        self.__portas = portas

    def __str__(self) -> str:
        return f"Carro - {super().__str__()}, Portas: {self.__portas}"


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cilindradas: int):
        self.__cilindradas = cilindradas
        super().__init__(marca, modelo)

    @property
    def cilindradas(self):
        return self.__cilindradas

    @cilindradas.setter
    def cilindradas(self, cilindradas):
        self.__cilindradas = cilindradas

    def __str__(self) -> str:
        return f"Moto - {super().__str__()}, Cilindradas: {self.__cilindradas}"


carro = Carro("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR500R", 500)
veiculo = [carro, moto]

for vl in veiculo:
    print(vl)





