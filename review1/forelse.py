nums = [1, 3, 6, 10, 12, 3, 5]

contem_negativos = True

for n in nums:
    if n < 0:
        break

else:
    contem_negativos = False


if contem_negativos:
    print("A lista contém números negativos")

else:
    print("A lista NÃO contém números negativos")
