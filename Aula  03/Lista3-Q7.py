total_geral = 0

print("Cardápio da Lanchonete")
print("----------------------")
print("Especificação   Código   Preço")
print("Cachorro Quente 100      R$ 1,20")
print("Bauru Simples   101      R$ 1,30")
print("Bauru com ovo   102      R$ 1,50")
print("Hambúrguer      103      R$ 1,20")
print("Cheeseburguer   104      R$ 1,30")
print("Refrigerante    105      R$ 1,00")

while True:
    codigo = int(input("Digite o código do item (-1 para encerrar): "))
    if codigo == -1:
        break

    if codigo not in [100, 101, 102, 103, 104, 105]:
        print("Código inválido. Tente novamente.")
        continue

    quantidade = int(input("Digite a quantidade desejada: "))

    if codigo == 100:
        preco_item = 1.20
    elif codigo == 101:
        preco_item = 1.30
    elif codigo == 102:
        preco_item = 1.50
    elif codigo == 103:
        preco_item = 1.20
    elif codigo == 104:
        preco_item = 1.30
    elif codigo == 105:
        preco_item = 1.00

    valor_total = preco_item * quantidade
    total_geral += valor_total

    print("Item:", codigo)
    print("Quantidade:", quantidade)
    print("Valor a ser pago:", valor_total)
    print()

print("Total geral do pedido: R$", total_geral)
