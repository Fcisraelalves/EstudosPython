#Exercício #15

lista = [1,1,1,2,2,2,3,3,3,4,5,6,6,6,7,7]
listaUnica = []
for numero in lista:
    if not numero in listaUnica:
        listaUnica.append(numero)

print(f"Lista original: {lista}")
print(f"Lista sem duplicatas: {listaUnica}")

