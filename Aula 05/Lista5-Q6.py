numeros = []
qtd_pares = 0

for i in range(5):
    numeros.append(int(input("Digite um numero: ")))

for i in range(5):
    if numeros[i] % 2 == 0:
        qtd_pares+=1

print("Quantidade de números pares: ", qtd_pares)

