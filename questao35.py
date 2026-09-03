produtos = {}
for i in range(1, 4):
    nome = input(f"Nome do produto {i}: ")
    quantidade = int(input(f"Quantidade de {nome}: "))
    produtos[nome] = quantidade
print("Produtos cadastrados:", produtos)
