matriz = [[-2, 4, 0], [5, -1, 8], [-3, 7, 6]]
quantidade = 0
for linha in matriz:
    for valor in linha:
        if valor > 0:
            quantidade += 1
print(f"Quantidade de valores positivos: {quantidade}")
