class Carro:
    def __init__(self):
        self.pass_ = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100
        
    def __str__(self):
        return f"pass: {self.pass_}, gas: {self.gas}, km: {self.km}"

    def show(self):
        print(self)

    def enter(self):
        if self.pass_ >= self.passMax:
            print("fail: limite de pessoas atingido")
        else:
            self.pass_ += 1

    def leave(self):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pass_ -= 1
          
    def fuel(self, amount: int) -> None:
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distancia: int):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas < distancia:
            dirigido = self.gas
            self.km += dirigido
            self.gas = 0
            print(f"fail: tanque vazio apos andar {dirigido} km")
        else:
            self.km += distancia
            self.gas -= distancia
        

def main():
    carro = Carro()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            if args[1:]:
                carro.fuel(int(args[1]))
            else:
                print("fail: comando invalido")
        elif args[0] == "drive":
            if args[1:]:
                carro.drive(int(args[1]))
            else:
                print("fail: comando invalido")

main()