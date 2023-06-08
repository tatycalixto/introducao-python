from datetime import date,timedelta
agenda = {}
data_atual = date.today()
data_texto = data_atual.strftime('%d/%m/%Y')

data_amanha = data_atual + timedelta(days=1)
data_texto_amanha = data_amanha.strftime('%d/%m/%Y')


nome = input("Digite seu nome: ")
compromisso = input("Digite seu compromisso: ")
data = input("Digite a data no formato DD/MM/AAAA: ")

agenda["Nome"] = nome
agenda["compromisso"] = compromisso
agenda["data"]= data

if data_texto in agenda.values():
    print("Você tem compromisso Hoje!")
elif data_texto_amanha in agenda.values():
    print("Você tem compromisso Amanhã!")
else:
    print("Você não tem compromisso!")
