class Towel:
    def __init__(self, color: str, size: str):
        self.color = 'white'
        self.size = 'm'
        self.wetness = 0
    
    def __str__(self):
        return f'color:{self.color}, tam: {self.size}, um: {self.wetness}'


towel = Towel('green', 'g') #objetos
toalha = Towel('red', 'p')
outra = toalha
outra.color = 'blue'
toalha.color = 'yellow'


print(towel.color)
print(towel.size)
print(towel.wetness)
