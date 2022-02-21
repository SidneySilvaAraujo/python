#formatação de strings
print("O {} é {}".format("Python", "de mais!"))
#Formatação de strings com id
print("O {1} é {0}!".format("Python", "de mais"))
#Podemos alterar a ordem da formatação, apenas trocando o id, dentro das chaves.
#Os ids, comessam em 0, 1, ETC

#formatação de floats
print("seu saldo é: {:.2f}!".format(110.25))
#Dentro das chaves, definimos, que ela vai receber um float.
#e também, que averão apenas duas casas decimais.
#Formatação de inteiros.
print("Data: {:02d}/{:02d}/{:04d}".format(21, 2, 2022))


