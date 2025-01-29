matriz = []
for l in range(2):
    linha = []
    for c in range(3):
        num = int(input(f"Digite o número {c + 1} para a lista {l + 1}: "))
        linha.append(num)
    matriz.append(linha)
transposta = []
for j in range(3):
    nova_linha = []
    for i in range(2):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)
    print()
    
print("Matriz original:")
for linha in matriz:
    print(linha)
    
print("Matriz transposta:")
for linha in transposta:
    print(linha)