with open("alunos.txt","r",encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    qtd_alunos = len(linhas)

print("A quantidade de aluno é: ",qtd_alunos)

