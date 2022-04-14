contagem = 10

while contagem > 0:
    print(contagem)
    contagem -= 1
    # contagem = contagem - 1
    if contagem == 2:
        print("Contagem foi interrompida")
        break

else:
    print("Contagem finalizada")
