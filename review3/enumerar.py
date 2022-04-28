def sequencia_infinita(num_inicial:int=0, passo:int=1):
    v = num_inicial

    while True:
        yield v
        v += passo


def enumerar(sequencia, indice:int=0):
    secundaria = sequencia_infinita(indice)

    for item in sequencia:
        yield (next(secundaria), item)


def main():
    frutas = ["banana", "melancia", "morango"]
    enumerado = enumerar(frutas)

    for (indice, fruta) in enumerado:
        print(f"frutas[{indice}] = {fruta}")

if __name__ == '__main__':
    main()
