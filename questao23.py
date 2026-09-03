quantidade = int(input("Quantos gastos deseja informar? "))
gastos = []
for i in range(quantidade):
    gastos.append(float(input(f"Gasto {i + 1}: R$ ")))
print(f"Soma dos gastos: R$ {sum(gastos):.2f}")
