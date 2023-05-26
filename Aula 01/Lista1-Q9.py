kg_peixe = float(input("Digite o kg do peixe: "))

if  kg_peixe > 50:
    kg_e = kg_peixe - 50
    multa = kg_e * 4
    print("O valor da multa é R$ ",multa)
else:
    print("Não teve multa!")
