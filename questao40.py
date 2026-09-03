import random
sorteado = random.randint(1, 100)
while True:
    tentativa = int(input("Tente adivinhar o numero de 1 a 100: "))
    if tentativa == sorteado:
        print("Acertou!")
        break
    if tentativa < sorteado:
        print("O numero procurado e maior.")
    else:
        print("O numero procurado e menor.")
