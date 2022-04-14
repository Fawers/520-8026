# Baby Boomer Até 1964
# Geração X 1965 - 1979
# Geração Y 1980 - 1994
# Geração Z 1995 - Atual

def nome_geracao(ano: int) -> str:
    if ano <= 1964:
        g = 'Baby Boomer'

    elif ano <= 1979:
        g = 'X'

    elif ano <= 1994:
        g = 'Y'

    else:
        g = 'Z'

    return g

def nome_geracao_com_dicionarios(ano: int) -> str:
    geracoes = {
        1964: 'Baby Boomer',
        1979: 'X',
        1994: 'Y',
    }

    for k in geracoes:
        if ano <= k:
            return geracoes[k]

    # ↓↓ desnecessário
    else:
        return 'Z'

def main2():
    ano = int(input("Em que ano você nasceu? "))
    geracao = nome_geracao_com_dicionarios(ano)

    print(f"Você pertence à geração {geracao}")

def main():
    ano = int(input("Em que ano você nasceu? "))
    geracao = nome_geracao(ano)

    print(f"Você pertence à geração {geracao}")


if __name__ == '__main__':
    main2()
