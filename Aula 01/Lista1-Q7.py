km_percorrido = float(input("Digite os km percorridos: "))
dia = int(input("Digite a quantidade de dias que você vai ficar com o carro: "))

aluguel = dia * 60
valor_km_percorridos = 0.15 * km_percorrido

print("Você vai pagar R$ ",aluguel+valor_km_percorridos)