alunos = {}
for i in range(1, 6):
    nome = input(f"Nome do aluno {i}: ")
    nota = float(input(f"Nota de {nome}: "))
    alunos[nome] = nota
media = sum(alunos.values()) / len(alunos)
print(f"Media da turma: {media:.2f}")
print("Aprovados:")
for nome, nota in alunos.items():
    if nota >= 7:
        print(nome)
