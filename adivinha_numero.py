import random

print("OLÁ, IREI TESTAR A SUA INTELIGÊNCIA")
print("Selecione um intervalo de números", end=" ")
print("que irei pensar em um inteiro nesse intervalo.")
print("Depois disso você deverá descobrir em qual número estou pensando!")

inicio_intervalo = int(input("Digite o inicio do intervalo: "))
fim_intervalo = int(input("Digite o final do intervalo: "))

numero_aleatorio = random.randint(inicio_intervalo, fim_intervalo)

print(f"PENSEI EM UM NÚMERO ENTRE {inicio_intervalo} E {fim_intervalo}")

palpite = int(input("Digite seu palpite: "))

while (palpite != numero_aleatorio):
    if palpite > numero_aleatorio:
        print("ERROU! Digite um número menor")
    elif palpite < numero_aleatorio:
        print("ERROU! Digite um número maior")

print(f"Você ACERTOU! Estava pensando no número {numero_aleatorio}")
