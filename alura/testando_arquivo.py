palavras = open("Palavras.txt", "w")
palavras.write("banana\n manga \n")
palavras.close()
palavras = open("palavras.txt", "r")
for linha in palavras:
    print(linha)
palavras.close()
palavras = open("palavras.txt", "a")
palavras.write("pera \n uva\n")
palavras.close()
palavras = open("palavras.txt", "r")
for linha in palavras:
    print(linha)
palavras.close()

