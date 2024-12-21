#Exercício #11

import random as rd

lista = [rd.randint(1,10) for _ in range(10)]

print(f"A minha lista antes da remoção é {lista}")


for elemento in lista.copy():
    if lista.count(elemento) != 1:
        lista.remove(elemento)

print(f"A minha lista após as remoções é {lista}.")