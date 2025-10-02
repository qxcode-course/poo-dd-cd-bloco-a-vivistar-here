

class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0

    def dry(self, amount:int) -> None:
        self.wetness += amount
        if self.wetness >= self.isMaxWetness():
            self.wetness = self.isMaxWetness()
            print("toalha encharcada")

    def wringOut(self):
        self.wetness = 0

    def isMaxWetness (self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0
    
    def __str__(self) -> str:
        return f'cor:{self.color}, tam:{self.size}, um:{self.wetness}'
    
def main():
    towel: Towel = Towel(" azul", " P")
