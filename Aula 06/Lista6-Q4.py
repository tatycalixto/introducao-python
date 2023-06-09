def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    cpf = input("Digite o CPF da pessoa: ")
    pessoa = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf
    }
    return pessoa

def remover_menores(dicionario_pessoas):
    menores = {}
    for cpf, pessoa in dicionario_pessoas.items():
        if pessoa["idade"] < 18:
            menores[cpf] = pessoa
    for cpf in menores:
        del dicionario_pessoas[cpf]
    return menores

def exibir_pessoas(dicionario_pessoas):
    print("\nPessoas cadastradas:")
    for pessoa in dicionario_pessoas.values():
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, CPF: {pessoa['cpf']}")


pessoas = {}
continuar = True
while continuar:
    pessoa = cadastrar_pessoa()
    cpf = pessoa["cpf"]
    pessoas[cpf] = pessoa
    opcao = input("Deseja cadastrar outra pessoa? (s/n): ")
    if opcao.lower() != "s":
        continuar = False


menores = remover_menores(pessoas)


exibir_pessoas(pessoas)
print("\n---\nPessoas menores de 18 anos:")
exibir_pessoas(menores)
