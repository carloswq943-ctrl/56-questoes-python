alunos = {}
for i in range(1, 6):
    nome = input(f"Nome do aluno {i}: ")
    nota = float(input(f"Nota de {nome}: "))
    alunos[nome] = nota
print("Registros:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")
