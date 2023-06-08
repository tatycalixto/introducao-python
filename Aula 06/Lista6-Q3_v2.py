from datetime import date,timedelta
agenda = {}

numero = int(input("Digite a quantidade de dados na agenda: "))

data_atual = date.today()
data_texto_atual = data_atual.strftime('%d/%m/%Y')

data_amanha = data_atual+timedelta(days=1)
data_texto_amanha = data_amanha.strftime('%d/%m/%Y')

for i in range(1,numero+1):
    nome = input("Digite o nome: ")
    compromisso = input("Digite o compromisso: ")
    data = input("Digite a data no formato DD/MM/AAAA: ")
    agenda[f"\nCompromisso{i}"] ={'Nome':nome,'Compromisso':compromisso,'Data':data} 

compromisso_hoje = None
compromisso_amanha= None

for compromisso in agenda.values():
    if compromisso ['Data'] == str(data_texto_atual):
        compromisso_hoje = compromisso
    if compromisso ['Data'] == str(data_texto_amanha):
        compromisso_amanha = compromisso

 
print("\nCompromissos:")
print("----------------")
if compromisso_hoje:
    print("Hoje:")
    print("Tipo de compromisso:", compromisso_hoje['Tipo'])
else:
    print("Não há compromissos marcados para hoje.")

if compromisso_amanha:
    print("Amanhã:")
    print("Tipo de compromisso:", compromisso_amanha['Tipo'])
else:
    print("Não há compromissos marcados para amanhã.")