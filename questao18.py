total = 0
for dia in range(1, 8):
    total += float(input(f"Vendas do dia {dia}: R$ "))
print(f"Faturamento semanal: R$ {total:.2f}")
