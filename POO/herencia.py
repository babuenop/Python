

class Rectangulo: 
    def __init__(self, base, altura):
        self.base=base 
        self.altura = altura
    def area (self):
        return self.base * self.altura
class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    Rectangulo =Rectangulo(base=3, altura=4)
    print(Rectangulo.area())
    Cuadrado = Cuadrado(lado=5)
    print(Cuadrado.area())
    pass