notas = {"Ana": 8.5, "Bruno": 7.0, "Carla": 9.2}
nome = input("Nome do estudante: ")
if nome in notas:
    print(f"Nota de {nome}: {notas[nome]}")
else:
    print("Estudante nao encontrado.")
