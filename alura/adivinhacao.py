print("Bem vindo ao jogo de adivinhação!")
tentativas = int(input("Informe quantas tentativas você deseja."))
rodada = 1
numero_secreto = 38
while (tentativas > 0):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute = int(input("Digite seu número."))
    if (numero_secreto == chute):
        print("Você digitou:", chute, "parabéns, você acertou!")
    elif (chute < numero_secreto):
        print("Você digitou:", chute, "o número é maior!")
    elif (chute > numero_secreto):
        print("Você digitou:", chute, "o número é menor!")
    tentativas = tentativas -1
    rodada = rodada + 1
print("Fim de jogo.")


