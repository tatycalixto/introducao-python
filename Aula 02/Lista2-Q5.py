numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
numero3 = float(input("Digite o número 3: "))

if numero1 > numero2 and numero1 > numero3:
    print("Número maior é ",numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Número maior é ",numero2)
else:
    print("Número maior é ",numero3)

if numero1 < numero2 and numero1 < numero3:
    print("Número menor é ",numero1)
elif numero2 < numero1 and numero2 < numero3:
    print("Número menor é ",numero2)
else:
    print("Número menor é ",numero3)