class Animal:
    def __init__(self, species: str, sound: str):
        self.species = species
        self.sound = sound
        self.age = 0

    def __str__(self) -> str:
        return f'species:{self.species}, sound:{self.sound}, age:{self.age}'

def main():
    
    while True:
        line = input()
        print("$" + line)
        args = line.split(' ')

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(Animal)
        else:
            print('fail: comando invalido')

        