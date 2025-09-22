
class Towel:
    def __init__(self, color: str, size: str):
        self.color = 'blue'
        self.size = 'p'
        self.wetness = 0

    def dry(self, amount:int) -> None:
        self.wetness += amount

    def getMaxWetness (self) -> int:
        if self.size == 'p':
            return 10
        if self.size == 'm':
            return 20
        if self.size == 'g':
            return 30
        return 0
    
    def __str__(self) -> str:
        return f'cor:{self.color}, tam:{self.size}, um:{self.wetness}'
    
    def isDry(self) -> bool:
        return self.wetness == 0
    
    def wringOut(self) -> None:
        self.wetness = 0

def main(): #2
    toalha = Towel('','') #objeto manipulado 3

    while True: #4 loop infinito
        line: str = input() #5 entrada de linha
        args: list[str] = line.split('') #6 lista de palavras

        if args[0] == 'end': #7 fim da execução
            break
        elif args[0] == 'new': #color size
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == 'show':
            print(toalha)
        elif args[0] == 'dry': # amount
            amount: int = int(args[1])
            toalha.dry(amount)

        else: #8 comando não encontrado
            print('fail: comando invalido')




main() #1