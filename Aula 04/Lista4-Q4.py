frase = input("Digite uma frase: ")

espacos = 0
vogais = 0

for caractere in frase:
    if caractere == ' ':
        espacos += 1
    elif caractere in 'aeiouAEIOU':
        vogais += 1

print("Quantidade de espaços em branco:", espacos)
print("Quantidade de vogais:", vogais)
