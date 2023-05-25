preco = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o desconto que você terá: "))

valor_desconto = (preco*desconto)/100
preco = preco - valor_desconto #preco -= valor_desconto
print("Valor com desconto - R$ ",preco)
print("Desconto: ", desconto,"%")

