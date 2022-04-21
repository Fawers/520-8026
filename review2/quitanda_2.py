class Fruit:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ($ {self.price:.2f})"

    def __repr__(self):
        return f"Fruit('{self.name}', {self.price})"


class Menu:
    def __init__(self, title: str, options: list[str], input_text: str):
        self.title = title
        self.options = options
        self.input_text = input_text

    def show_title(self):
        edges = '=' * 5
        print(f"{edges} {self.title} {edges}")

    def show_options(self):
        enumerated_options = enumerate(self.options, 1)

        for (op, desc) in enumerated_options:
            print(f"{op}: {desc}")

    def get_input(self) -> str | None:
        user_input = input(self.input_text)

        try:
            option = int(user_input)

            if option <= 0:
                raise IndexError()

            return self.options[option-1]

        except:
            return None

    def show(self) -> str:
        self.show_title()
        self.show_options()
        i = self.get_input()

        while i is None:
            print("Opção inválida.")
            i = self.get_input()

        return i

MARKET = [
    Fruit("Banana", 3.50),
    Fruit("Melancia", 7.50),
    Fruit("Morango", 5.00),
]

def menu_market(basket: dict[Fruit, int]):
    market = Menu(
        "Quitanda",
        ['Ver cesta', 'Adicionar frutas', 'Checkout', 'Sair'],
        "Digite a opção desejada: ")

    while True:
        i = market.show()
        if i == "Ver cesta":
            print(basket)

        elif i == 'Adicionar frutas':
            f = menu_fruits()

            if f in basket:
                basket[f] += 1

            else:
                basket[f] = 1

        elif i == 'Checkout':
            print("Total: $", checkout(basket))

        else:
            break

    print("Volte sempre!")


def menu_fruits():
    menu = Menu(
        'Frutas',
        MARKET,
        'Digite a opção da fruta desejada: ')

    return menu.show()

def checkout(basket: dict[Fruit, int]):
    total = 0.0

    for (fruit, qty) in basket.items():
        total += fruit.price * qty

    return total

def main():
    basket: dict[Fruit, int] = {}
    menu_market(basket)


if __name__ == '__main__':
    main()
