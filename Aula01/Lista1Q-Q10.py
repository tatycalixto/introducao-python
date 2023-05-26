tamanho_metros = float(input("Digite o tamanho em metros: "))

#saber quantos litros preciso para pintar 
qtd_litros = int(tamanho_metros/3)
if tamanho_metros % 3 !=0:
   qtd_litros =  qtd_litros + 1

#saber a quantidade de latas de tintas que precisa comprar
qtd_latas = int(qtd_litros/18)
if qtd_litros % 18 !=0:
   qtd_latas = qtd_latas+1

print("Quantidade de latas de tinta a serem compradas: ",qtd_latas)
print("Preço Total: R$ ", qtd_latas*80)
