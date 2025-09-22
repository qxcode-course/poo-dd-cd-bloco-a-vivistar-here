class Towel:
    def __init__(self, color: str, size: str): #método construtor, constrói a classe do objeto
        self.color = 'white'
        self.size = 'm'
        self.wetness = 0
    
    def __str__(self):
        return f'color:{self.color}, tam: {self.size}, um: {self.wetness}'
    def __use__(self, quantidade) #recebe o valor
        self.wetness = quantidade #wtness aumenta pelo valor passado (ex:15, 20, etc)
        print('Towel was used. Wetness at {self.wetness}' )


towel = Towel('green', 'g') #objetos

#por que esse código tava tão longe...