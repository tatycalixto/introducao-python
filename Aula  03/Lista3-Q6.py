print("Tabela de Preços")
print("----------------")

preco_unitario = 1.99

for quantidade in range(1, 51):
    valor_total = quantidade * preco_unitario
    print(quantidade, " - R$", valor_total)