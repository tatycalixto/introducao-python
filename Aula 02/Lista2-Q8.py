print("Respondas as perguntas com S ou N")
p1 = input("Telefonou para a vítima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Mora perto da vítima? ") 
p4 = input("Devia para a vítima? ") 
p5 = input("Já trabalhou com a vítima? ")
respostas = 0
if p1 =="S":
    respostas+=1
if p2 =="S":
    respostas+=1
if p3 =="S":
    respostas+=1
if p4 =="S":
    respostas+=1
if p5 =="S":
    respostas+=1

if respostas == 2:
    print("Suspeita!")
elif respostas >=3 and respostas <=4:
    print("Cúmplice!")
elif respostas == 5:
    print("Assassino!")
else:
    print("Inocente!")

