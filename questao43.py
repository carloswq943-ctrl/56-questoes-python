matriz = [[4, 8, 2], [9, 1, 6], [3, 7, 5]]
maior = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor
print(f"Maior valor: {maior}")
