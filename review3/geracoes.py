# Baby Boomer Até 1964
# Geração X 1965 - 1979
# Geração Y 1980 - 1994
# Geração Z 1995 - Atual


class InvalidYear(Exception):
    pass


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


def main():
    while True:
        try:
            ano = int(input("Em que ano você nasceu? "))

            if ano < 1930 or ano > 2022:
                raise InvalidYear(ano)

        except ValueError:
            print("Digite um número válido.")

        except InvalidYear as iy:
            print(f"{iy.args[0]} não é um ano válido.")

        else:
            geracao = nome_geracao(ano)
            print(f"Você pertence à geração {geracao}")
            break


if __name__ == '__main__':
    main()
