#Exercício #10

frase = str(input("insira uma frase: "))

if not frase == "":

    palavras = frase.split()

    palavras.sort(key=len)

    print(f"A maior palavra da frase é {palavras[-1]}")

else:
    print(f"Erro: digite uma frase válida.")