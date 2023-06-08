dados_usuario = {}

nome = input("Digite seu nome: ")
idade = int(input("Digite sua Idade: "))
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereco: ")

dados_usuario["Nome"] = nome
dados_usuario["Idade"] = idade
dados_usuario["Telefone"] = telefone
dados_usuario["Endereco"] = endereco

for chave,valor in dados_usuario.items():
    print(chave,": ", valor)
