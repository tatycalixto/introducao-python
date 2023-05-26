nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1+nota2)/2

if media >=7:
    print("Aprovado! Sua média foi: ",media)
elif media == 10:
    print("Aprovado com Distinção! Sua média foi: ",media)
else:
    print("Reprovado! Sua média foi: ",media)
