lista_idade = []
lista_altura = []

for i in range(5):
    lista_idade.append(int(input("Digite a idade: ")))
    lista_altura.append(float(input("Digite a altura: ")))

lista_idade.reverse()
lista_altura.reverse()

print("As idades são:", lista_idade)
print("As alturas: ",lista_altura)