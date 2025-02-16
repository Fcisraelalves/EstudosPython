# 3. Crie um programa que leia um valor N, tal que N > 0. O pro-
# grama deve gerar duas listas aleatórias (L1 e L2), com valores
# no intervalo [1 e 10]. A terceira lista, L3, deve ser gerada com
# base na soma entre os elementos de L1 e de L2. Ao fim, o pro-
# grama deve imprimir as 3 listas.

import random as rd

N = int(input("insira o valor de N: "))
while N <= 0:
  print(f"ERRO: N <= 0")
  N = int(input("insira o valor de N: "))

L1 = [rd.randint(1, 10) for _ in range(N)]
L2 = [rd.randint(1, 10) for _ in range(N)]

L3 = [L1[i] + L2[i] for i in range(N)]

print(f"L1: {L1}")
print(f"L2: {L2}")
print(f"L3: {L3}")
