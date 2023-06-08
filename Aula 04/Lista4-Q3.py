palavra = input("Digite uma palavra: ")

invertida = ''

for i in range(len(palavra)-1, -1, -1):
    invertida += palavra[i]

print("Palavra original:", palavra)
print("Palavra invertida:", invertida)

if palavra == invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
