
def jogar():
    print("Bem vindo ao jogo da forca!")
    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    while (not acertou and not enforcou):
        chute = str(input("qual letra?"))
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição: {}".format(chute, index))
                index = index +1
    print("Fim de jogo.")

