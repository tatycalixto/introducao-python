soma = 0
with  open("numeros.txt","r") as arquivo:
    numeros = arquivo.readlines()

for numero in numeros:
    soma+=int(numero.strip())

print("A soma é: ",soma)
