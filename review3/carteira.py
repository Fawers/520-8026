def nova_carteira(v: float):
    if v < 0:
        raise ValueError("v negativo")

    return {"grana": v}

def comprar(carteira:dict[str, float], preco: float) -> bool:
    pode_comprar = carteira['grana'] >= preco

    if pode_comprar:
        # só entra nesse bloco se
        # a condição for true
        carteira['grana'] -= preco

    # não tem else, então não tem bloco pro
    # caso falso

    return pode_comprar

carteira = nova_carteira(50.0)

def a(b: bool) -> str | None:
    return "bOoLeAn" if b else None

def b():
    s = a(True)

    if s is not None:
        print(s.title())

    else:
        print(s)
