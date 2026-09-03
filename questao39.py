import random
sorteado = random.randint(1, 10)
tentativa = int(input("Adivinhe o numero de 1 a 10: "))
if tentativa == sorteado:
    print("Voce acertou!")
else:
    print(f"Voce errou. O numero era {sorteado}.")
