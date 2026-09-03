total = 0
for i in range(1, 6):
    quantidade = int(input(f"Quantidade arrecadada pelo voluntario {i}: "))
    total += quantidade
print(f"Total arrecadado: {total}")
