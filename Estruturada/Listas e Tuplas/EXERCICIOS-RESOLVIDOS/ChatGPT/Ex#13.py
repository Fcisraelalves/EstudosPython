#Exercício #13

matriz = ((1,2,3),
         (4,5,6),
         (7,8,9))

soma = 0

indice = 0
for linha in matriz:
    soma += linha[indice]
    indice += 1

for linha in matriz:
    for elemento in linha:
        print(f"{elemento} ", end="")
    print()

print(f"A soma dos elementos da diagonal principal da matriz é {soma}")