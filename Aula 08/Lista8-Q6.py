def inverter_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    # Lê o conteúdo do arquivo de entrada
    with open(nome_arquivo_entrada, 'r',encoding="utf-8") as arquivo_entrada:
        conteudo = arquivo_entrada.read()

    # Inverte o conteúdo
    conteudo_invertido = conteudo[::-1]

    # Escreve o conteúdo invertido no arquivo de saída
    with open(nome_arquivo_saida, 'w',encoding="utf-8") as arquivo_saida:
        arquivo_saida.write(conteudo_invertido)

    # Exibe o conteúdo invertido na tela
    print(conteudo_invertido)

# Teste do programa
nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")

inverter_arquivo(nome_arquivo_entrada, nome_arquivo_saida)
