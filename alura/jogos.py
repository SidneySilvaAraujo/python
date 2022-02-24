import adivinhacao
import forca
print("Escolha um jogo.")
print("*1 jogo da forca, *2 jogo de adivinhação.")
opcao = int(input("qual jogo?"))
if opcao == 1:
    print("jogando forca.")
    forca.jogar()
elif opcao == 2:
    print("Jogando adivinhação.")
    adivinhacao.jogar()



