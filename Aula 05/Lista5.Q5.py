lista_perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
lista_respostas = []
for i in range(5):
    print("Pergunta ", i+1, " ",lista_perguntas[i])
    lista_respostas.append(input("Resposta com s ou n: "))

qtd_respostas = lista_respostas.count('s')
print(qtd_respostas)

if qtd_respostas == 2:
    print("Suspeito!")
elif qtd_respostas ==3 or qtd_respostas ==4:
    print("Cúmplice!")
elif qtd_respostas == 5:
    print("Assassino!")
else:
    print("Inocente!")


