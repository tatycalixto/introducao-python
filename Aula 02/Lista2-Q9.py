n1 =  float(input("Digite a nota 1: "))
n2 =  float(input("Digite a nota 2: "))

media = (n1+n2)/2
print(media)
if media >= 9 and media <=10:
    print("A")
elif media >= 7.5 and media < 9:
    print("B")
elif media >=6 and media <7.5:
    print("C")
elif media >= 4 and media < 6:
    print("D")
else: 
    print("E")
