salario = float(input("Digite o valor do salário"))
aumento = float(input("Digite a porcentagem do aumento: ")) 

valor_aumento = (salario*aumento)/100
salario = salario + valor_aumento 
print("Aumento foi de : ", aumento,"%")
print("Seu salário será de - R$ ",salario)

