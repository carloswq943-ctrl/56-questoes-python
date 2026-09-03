soma = 0
while True:
    valor = float(input("Digite um valor (0 encerra): "))
    if valor == 0:
        break
    soma += valor
print(f"Soma: {soma}")
