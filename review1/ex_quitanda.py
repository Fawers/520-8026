from collections import defaultdict


QUITANDA = {'Banana': 3.5, 'Melancia': 7.50, 'Morango': 5.0}

# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair
#
# Digite a opção desejada:

def menu_quitanda(cesta: dict[str, int]):
    op_saida = 4
    op = 0

    while op != op_saida:
        print("===== QUITANDA =====")
        print("1: Ver cesta")
        print("2: Adicionar frutas")
        print("3: Checkout")
        print(f"{op_saida}: Sair")
        op_s = input("\nDigite a opção desejada: ")

        if not op_s.isdigit():
            print("Digite um número, seu asqueroso.\n")
            continue

        op = int(op_s)

        if op == 1:
            print(cesta)

        elif op == 2:
            fruta = menu_frutas()
            # Sem defaultdict:
            # if fruta in cesta:
            #     cesta[fruta] += 1
            # else:
            #     cesta[fruta] = 1

            # Com defaultdict:
            cesta[fruta] += 1
            print(f"{fruta} adicionada com sucesso!")

        elif op == 3:
            checkout(cesta)

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
    quitanda_enum = list(enumerate(QUITANDA, 1))
    for (op, desc) in quitanda_enum:
        print(f"{op}: {desc}")

    op = int(input("\nDigite a opção desejada: "))

    return quitanda_enum[op-1][1]


def checkout(cesta: dict[str, int]):
    total = 0.0

    for (fruta, qtd) in cesta.items():
        total += QUITANDA[fruta] * qtd

    print("Cesta: {}".format(', '.join(cesta.keys())))
    print("Total: I$ %.2f" % total)

def main():
    menu_quitanda(defaultdict(int))

if __name__ == '__main__':
    main()
