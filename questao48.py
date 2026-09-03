matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(1 if i == j else 0)
    matriz.append(linha)
for linha in matriz:
    print(linha)
