lista_notas = []

for i in range(4):
    lista_notas.append(float(input("Digite uma nota: ")))

soma = sum(lista_notas)
print("A média é: ",soma/4)
print("As notas: ", lista_notas)
