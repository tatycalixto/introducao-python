valor_saque = float(input("Digite o valor do saque: "))
contar_dinheiro = False
if valor_saque >=10 and valor_saque <=600:
    contar_dinheiro = True
else:
    print("Valor inválido para sacar dinheiro")
    

if contar_dinheiro:
    nota_cem = valor_saque // 100
    valor_saque = valor_saque % 100
    
    nota_cinquenta = valor_saque // 50
    valor_saque = valor_saque % 50

    nota_dez = valor_saque // 10
    valor_saque = valor_saque % 10

    nota_cinco = valor_saque // 5
    valor_saque = valor_saque % 5

    nota_um = valor_saque // 1
    print("Quantidade de notas fornecidas:\n")
    if nota_cem !=0:
        print("Notas de 100 reais:", int(nota_cem))
    if nota_cinquenta !=0:
        print("Notas de 50 reais:", int(nota_cinquenta))
    if nota_dez !=0:
        print("Notas de 10 reais:", int(nota_dez))
    if nota_cinco !=0:
        print("Notas de 5 reais:",int(nota_cinco))
    if nota_um !=0:
        print("Notas de 1 real:", int(nota_um))

