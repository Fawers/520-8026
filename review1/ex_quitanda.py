QUITANDA = ['Banana', 'Melancia', 'Morango']

# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair
#
# Digite a opção desejada:

def menu_quitanda(cesta: dict[str, int]):
    op_saida = 3
    op = 0

    while op != op_saida:
        print("===== QUITANDA =====")
        print("1: Ver cesta")
        print("2: Adicionar frutas")
        print("3: Sair")
        op_s = input("\nDigite a opção desejada: ")

        if not op_s.isdigit():
            continue

        op = int(op_s)

        if op == 1:
            print(cesta)

        elif op == 2:
            fruta = menu_frutas()
            cesta[fruta] += 1
            print(f"{fruta} adicionada com sucesso!")

        elif op != op_saida:
            print("Opção inválida.")

        print()

    print("Volte sempre!")

# Menu de frutas:
#
# Escolha fruta desejada:
# 1 - Banana
# 2 - Melancia
# 3 - Morango
#
# Digite à opção desejada: 2
# Melancia adicionada com sucesso!

def menu_frutas() -> str:
    for (op, desc) in enumerate(QUITANDA, 1):
        print(f"{op}: {desc}")

    op = int(input("\nDigite a opção desejada: "))

    return QUITANDA[op-1]


def main():
    cesta = {}

    for fruta in QUITANDA:
        cesta[fruta] = 0

    menu_quitanda(cesta)

if __name__ == '__main__':
    main()
