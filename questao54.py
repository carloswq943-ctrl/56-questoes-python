matriz = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
ocupadas = 0
for linha in matriz:
    ocupadas += sum(linha)
total = 3 * 3
print(f"Vagas ocupadas: {ocupadas}")
print(f"Vagas disponiveis: {total - ocupadas}")
