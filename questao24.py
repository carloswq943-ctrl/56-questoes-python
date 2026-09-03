nomes = input("Digite os nomes separados por virgula: ").split(",")
nomes = [nome.strip() for nome in nomes]
print("Ordem inversa:", nomes[::-1])
