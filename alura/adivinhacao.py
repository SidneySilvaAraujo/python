import random
print("Bem vindo ao jogo de adivinhação!")
tentativas = 0
print("Qual o nível de dificuldade?")
nivel = int(input("1 fácil, 2 médio, 3 dificil."))
if nivel == 1:
    print("Você terá 20 tentativas")
    tentativas = 20
elif nivel == 2:
    print("Você terá 10 tentativas.")
    tentativas = 10
else:
    print("Você terá 5 tentativas.")
    tentativas = 5
rodada = 1
numero_secreto = random.randrange(1, 101)
while (tentativas > 0):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute = int(input("Digite um número entre: 1 e 100"))
    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
    elif (numero_secreto == chute):
        print("Você digitou:", chute, "parabéns, você acertou!")
        break
    elif (chute < numero_secreto):
        print("Você digitou:", chute, "o número é maior!")
    elif (chute > numero_secreto):
        print("Você digitou:", chute, "o número é menor!")
    tentativas = tentativas -1
    rodada = rodada + 1
print("O número secreto era:     {}".format(numero_secreto))
print("Fim de jogo.")


