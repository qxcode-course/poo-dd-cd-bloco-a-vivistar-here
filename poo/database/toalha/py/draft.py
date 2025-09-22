class Towel:
    def __init__(self, color: str, size: str): #método construtor, constrói a classe do objeto
        self.color = 'white'
        self.size = 'm'
        self.wetness = 0

        def dry(self, amount:int) -> None: # type: ignore
            self.wetness += amount # type: ignore
        def getMaxWetness (self) -> int: # type: ignore
            if self.size == 'P': # type: ignore
                return 10
            if self.size == 'M': # type: ignore
                return 20
            if self.size == 'G': # type: ignore
                return 30
            
    def __str__(self): #toString
        return f'cor:{self.color}, tam:{self.size}, um:{self.wetness}'
  

minha = Towel('white', 'm') #objetos

#por que esse código tava tão longe...