lista_numeros = []
mult = 1
for i in range(5):
    lista_numeros.append(float(input("Digite um número: ")))
    mult*=lista_numeros[i] #mult = mult * lista_numeros[i]

soma = sum(lista_numeros)
print("As notas: ", lista_numeros)
print("A multiplicação: ",mult)