class Carro:
    def __init__(self):
        self.pass_ = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100
        
    def __str__(self):
        return f"pass:{self.pass_}, gas:{self.gas}, km:{self.km}"

    def mostrar(self):
        print(self)

    def entrar(self):
        if self.pass_ < self.passMax:
            self.pass_ += 1
        else:
            print("fail: limite de pessoas atingido")

    def sair(self):
        if self.pass_ > 0:
            self.pass_ -= 1
        else:
            print("fail: nao ha ninguem no carro")
          
    def abastecer(self, amount: int) -> None:
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def dirigir(self):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("tanque vazio")
            return
        else:
            self.km += self.gas
            print("fail: tanque vazio após andar {self.gas} km")
            self.gas = 0

    