# Criar o dicionário "traducao"
traducao = {
    'apple': 'maçã',
    'banana': 'banana',
    'car': 'carro',
    'house': 'casa',
    'dog': 'cachorro'
}

# Função para traduzir uma palavra em inglês
def traduzir(palavra):
    if palavra in traducao:
        return traducao[palavra]
    else:
        return 'Tradução não encontrada'

# Exemplos de uso da função
print(traduzir('apple'))  
print(traduzir('cat'))    
print(traduzir('house'))  
