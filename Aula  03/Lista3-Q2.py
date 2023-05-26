nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while nome == senha:
    print("Senha incorreta!")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

print("Nome: ",nome,"Senha: ",senha)
