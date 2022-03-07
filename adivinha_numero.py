import random
import math

print("OLÁ, IREI TESTAR A SUA INTELIGÊNCIA")
print("Selecione um intervalo de números", end=" ")
print("que irei pensar em um inteiro nesse intervalo.")
print("Depois disso você deverá descobrir em qual número estou pensando!")

inicio_intervalo = int(input("Digite o inicio do intervalo: "))
fim_intervalo = int(input("Digite o final do intervalo: "))

numero_aleatorio = random.randint(inicio_intervalo, fim_intervalo)
print(f"PENSEI EM UM NÚMERO ENTRE {inicio_intervalo} E {fim_intervalo}")

numero_tentativas = int(math.log(fim_intervalo - inicio_intervalo + 1, 2))
print(f"Você tem {numero_tentativas} TENTATIVAS!")

palpite = int(input("Digite seu palpite: "))
contador_tentativas = 0

while (contador_tentativas != numero_tentativas):
    if palpite > numero_aleatorio:
        contador_tentativas += 1
        print("ERROU! Digite um número menor")
        palpite = int(input("Digite seu palpite: "))
    elif palpite < numero_aleatorio:
        contador_tentativas += 1
        print("ERROU! Digite um número maior")
        palpite = int(input("Digite seu palpite: "))
    elif palpite == numero_aleatorio:
        print(f"Você ACERTOU! Estava pensando no número {numero_aleatorio}")
        break
