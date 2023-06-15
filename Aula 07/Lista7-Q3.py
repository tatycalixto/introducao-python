# Criar o dicionário "estoque"
estoque = {
    'banana': 10,
    'maçã': 5,
    'uva': 15,
    'laranja': 8,
    'morango': 20
}

# Função para verificar o estoque
def verifica_estoque(produto, quantidade):
    if produto in estoque:
        if estoque[produto] >= quantidade:
            return True
    return False

# Exemplos de uso da função
print(verifica_estoque('banana', 5))   
print(verifica_estoque('uva', 20))    
print(verifica_estoque('laranja', 10)) 
