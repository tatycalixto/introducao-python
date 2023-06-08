dic = {"Nome":"Maria","Idade":32,"Cidade":"Recife"}
dic["Profissao"]= "Programadora"
print(dic)
dic["Idade"] = 30
print(dic)

for chave,valor in dic.items():
    print(chave, ": ",valor)