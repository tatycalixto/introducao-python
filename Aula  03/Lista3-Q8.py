gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

while True:
    respostas = []
    acertos = 0

    print("\nGabarito da Prova")
    print("-----------------")
    for i in range(10):
        print(f"{i+1:02d} - {gabarito[i]}")

    for i in range(10):
        resposta = input(f"\nDigite a resposta da questão {i+1}: ")
        respostas.append(resposta.upper())

    for i in range(10):
        if respostas[i] == gabarito[i]:
            acertos += 1

    print("\nResultado do Aluno")
    print("------------------")
    print("Total de acertos:", acertos)
    print("Nota:", acertos)

    resposta_final = input("\nOutro aluno vai utilizar o sistema? (S/N): ")
    if resposta_final.upper() == 'N':
        break

print("\nEncerrando o programa...")
