quantidade_numeros = int(input("Digite a quantidade de números: "))
maior = 0
menor = 0
primeira = True
soma = 0

for i in range(quantidade_numeros):
    numero = int(input("Digite um número: "))
    soma +=numero #soma = soma + numero
    if primeira: 
        maior = numero
        #print("Primeira vez maior ",maior)
        menor = numero
        #print("Primeira vez menor ",menor)
        primeira = False
    if numero > maior:
        maior = numero
        #print("Modificando a variável maior ",maior)
    if numero < menor:
        menor = numero
        #print("Modificando a variável menor ",menor)
    

print("Maior número: ", maior)
print("Menor número: ",menor)
print("Soma dos  números: ",soma)

