livros = []
for i in range(1, 4):
    livros.append(input(f"Digite o titulo do livro {i}: "))
print("Livros cadastrados:")
for livro in livros:
    print(livro)
