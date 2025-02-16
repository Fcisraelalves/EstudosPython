# 2. Crie um programa no qual o usuário digite o número de
# linhas e o número de colunas de uma matriz M. Ao fim, o
# programa deve informar se M é uma matriz triangular infe-
# rior.

matriz = []
linha_atual = []
linhas = int(input("Insira a quantidade de linhas: "))
colunas = int(input("Insira a quantidade de colunas: "))

eh_inferior = True
for i in range(linhas):
  for j in range(colunas):
    linha_atual.append(int(input(f"matriz[{i}][{j}] = ")))
    if i < j and linha_atual[j] != 0:
      eh_inferior = False
  matriz.append(linha_atual.copy())
  linha_atual.clear()

print("Matriz:")
for linha in matriz:
  print(linha)
print()

print(f"é triangular inferior") if eh_inferior else print(f"não é triangular inferior")

