class Triangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def area(self):
        return (self.base * self.altura) / 2
