class Car:
    


def main():
    while True:
        line = input()
        print("$" + line)

        par = line.split(" ")
        cmd = par[0]

        if cmd == "end":
            break
        elif cmd == "show":
            # MOSTRE O CARRO
            pass
        elif cmd == "enter":
            # TENTE EMBARCAR UMA PESSOA
            pass
        elif cmd == "leave":
            # TENTE DESEMBARCAR UMA PESSOA
            pass
        elif cmd == "fuel":
            # INCREMENTE O COMBUSTIVEL
            # increment = int(par[1])
            pass
        elif cmd == "drive":
            # TENTE DIRIGIR CERTA DISTANCIA
            # distance = int(par[1])
            pass
        else:
            print("fail: comando invalido")

if __name__ == "__main__":
    main()

