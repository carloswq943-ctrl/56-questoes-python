temperaturas = []
for i in range(1, 6):
    temperaturas.append(float(input(f"Temperatura do dia {i}: ")))
media = sum(temperaturas) / len(temperaturas)
print(f"Media: {media:.2f} C")
if 18 <= media <= 28:
    print("A media esta na faixa ideal de cultivo.")
else:
    print("A media esta fora da faixa ideal de cultivo.")
print("Temperaturas cadastradas:", temperaturas)
