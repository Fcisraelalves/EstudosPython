#Exercício #12 

lista = []

for i in range(5):
    nome = str(input(f"insira o {i+1}º nome: "))
    idade = int(input(f"insira a idade de {nome}: "))
    lista.append((nome,idade))

print(f">>> Lista de tuplas não ordenada: ")
for tupla in lista:
    print(tupla)

trocou = True
while trocou:
    trocou = False
    tamanho = len(lista)
    for i in range(tamanho - 1):
        if lista[i][1] > lista[i+1][1]:
            aux = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = aux
            trocou = True

print(f">>> Lista de tuplas ordenada: ")
for tupla in lista:
    print(tupla)