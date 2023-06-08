# Lista de preços dos itens
precos = [15.90, 9.50, 7.80, 12.50, 6.20]

# Valor total inicialmente é zero
valor_total = 0

# Loop para calcular o valor total
while True:
    item = input("Digite o código do item (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja encerrar o programa
    if item.lower() == "sair":
        break
    
    try:
        # Converte o código do item para um índice válido na lista de preços
        codigo_item = int(item)
        
        # Verifica se o código do item é válido
        if codigo_item >= 0 and codigo_item < len(precos):
            valor_total += precos[codigo_item]
        else:
            print("Código do item inválido.")
    except ValueError:
        print("Código do item inválido.")
    
# Exibe o valor total da mesa
print("Valor total da mesa: R$", valor_total)
