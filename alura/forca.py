
def jogar():
    print("Bem vindo ao jogo da forca!")
    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    while (not acertou and not enforcou):
        chute = str(input("qual letra?"))
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(chute)
    print("Fim de jogo.")

