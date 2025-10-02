class Animal:
    def __init__(self, species: str, sound: str):
        self.species = species
        self.sound = sound
        self.age = 0

    def ageBy(self, increment: int) -> None:
        self.age += increment
        if self.age >= 4:
            print(f"Warning:{self.species} morreu")

    def makeSound(self = str):
        if self.age == 0:
            return "---"
        elif self.age == 4:
            return "RIP"
        return self.sound

    def __str__(self) -> str:
        return f'species:{self.species}, sound:{self.sound}, age:{self.age}'




def main():
    animal: Animal = Animal(" "," ")
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            species: str = args[1]
            sound: str = args[2]
            animal = Animal(species, sound)
        elif args

main()

        