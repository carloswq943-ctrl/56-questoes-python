medicamentos = {}
for i in range(1, 6):
    nome = input(f"Nome do medicamento {i}: ")
    quantidade = int(input(f"Quantidade de {nome} em estoque: "))
    medicamentos[nome] = quantidade
consulta = input("Digite o medicamento para consultar: ")
if consulta in medicamentos:
    print(f"Estoque de {consulta}: {medicamentos[consulta]}")
else:
    print("Medicamento nao cadastrado.")
