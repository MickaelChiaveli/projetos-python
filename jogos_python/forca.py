# forca.py

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "canoa".upper()
    letras_acertadas = ["_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
                #para cada letra da palavra secreta que o chute for igual, mostre a letra e o índice
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 6

        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar()