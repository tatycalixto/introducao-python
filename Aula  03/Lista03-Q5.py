numero = int(input("Digite um número inteiro: "))
inicio = int(input("Digite o valor inicial da tabuada: "))
fim = int(input("Digite o valor final da tabuada: "))

for i in range(inicio, fim + 1):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)