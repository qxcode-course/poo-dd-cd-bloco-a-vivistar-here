class Calculadora:
    def __init__(self, batteryMax: int):
        self.batteryMax = batteryMax
        self.battery = 0
        self.display = 0.0
    
    def change(self, value: int):
        self.battery += value
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a: int, b: int):
        if self.battery == 0:
            print("bateria insuficiente")
            return
        self.battery -= 1
        self.display =  a + b

    def div(self, num: int, den: int):
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return
        if den == 0:
            print("fail: divisao por zero")
            self.battery -= 1
            return
        self.battery -= 1
        self.display = num / den

    def __str__(self):
        return f"display = {self.display}, battery = {self.battery}"
    