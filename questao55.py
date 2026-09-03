disciplinas = ("Matematica", "Portugues")
alunos = {}
for i in range(1, 4):
    nome = input(f"Nome do aluno {i}: ")
    matematica = float(input("Nota de Matematica: "))
    portugues = float(input("Nota de Portugues: "))
    alunos[nome] = {"Matematica": matematica, "Portugues": portugues}
for nome, notas in alunos.items():
    media = (notas["Matematica"] + notas["Portugues"]) / 2
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    print(f"{nome}: media {media:.2f} - {situacao}")
print("Disciplinas:", disciplinas)
