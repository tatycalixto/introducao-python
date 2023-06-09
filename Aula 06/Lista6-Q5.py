def fazer_backup(dicionario_principal, dicionario_backup):
    dicionario_backup.update(dicionario_principal)
    dicionario_principal.clear()

def exibir_dicionario(dicionario):
    print("Conteúdo do dicionário:")
    for chave, valor in dicionario.items():
        print(chave, "->", valor)
    print()


dicionario_principal = {}
dicionario_backup = {}


contador = 1
while True:
    chave = input("Digite a chave (ou 'sair' para encerrar): ")
    if chave.lower() == "sair":
        break
    valor = input("Digite o valor: ")
    dicionario_principal[chave] = valor

    if len(dicionario_principal) >= 5:
        fazer_backup(dicionario_principal, dicionario_backup)
        print("Realizando backup...")
        exibir_dicionario(dicionario_backup)


if dicionario_principal:
    print("Conteúdo do dicionário principal:")
    exibir_dicionario(dicionario_principal)


print("Conteúdo do dicionário de backup final:")
exibir_dicionario(dicionario_backup)
