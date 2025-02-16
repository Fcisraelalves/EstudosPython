# 1. Crie um programa para gerar duas matrizes quadradas aleató-
# rias (A e B), no intervalo [1, 10], de mesma ordem, a qual deve ser in-
# formada pelo usuário. Ao fim, o programa deve calcular e imprimir
# a soma entre os elementos de A que estão abaixo da diagonal prin-
# cipal com os elementos de B que estão acima da diagonal principal.

import random as rd

ordem = int(input("insira a ordem das matrizes: "))

matrizA = [[rd.randint(1,10) for _ in range(ordem)] for _ in range(ordem)]
matrizB = [[rd.randint(1,10) for _ in range(ordem)] for _ in range(ordem)]

soma = 0

for i in range(len(matrizA)):
  for j in range(len(matrizA[0])):
    if i < j:
      soma += matrizB[i][j]
    elif i > j:
      soma += matrizA[i][j]
print("Matriz A:")
for linha in matrizA:
  print(linha)
print()

print("Matriz B:")
for linha in matrizB:
  print(linha)
print()

print(f"A soma é: {soma}")
