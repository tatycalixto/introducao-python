# Criar o dicionário "idade"
idade = {
    'João': 30,
    'Maria': 25,
    'Pedro': 40,
    'Ana': 35,
    'Carlos': 28
}

# Função para verificar a idade de uma pessoa
def verificar_idade(nome):
    if nome in idade:
        return idade[nome]
    else:
        return 'Idade não encontrada'

# Exemplos de uso da função
print(verificar_idade('João'))   
print(verificar_idade('Lucas'))   
print(verificar_idade('Ana'))    
