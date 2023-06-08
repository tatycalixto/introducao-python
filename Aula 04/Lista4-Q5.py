data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

dia = data[:2]
mes = data[3:5]
ano = data[6:]

# Verifica o mês por extenso
if mes == "01":
    mes_extenso = "janeiro"
elif mes == "02":
    mes_extenso = "fevereiro"
elif mes == "03":
    mes_extenso = "março"
elif mes == "04":
    mes_extenso = "abril"
elif mes == "05":
    mes_extenso = "maio"
elif mes == "06":
    mes_extenso = "junho"
elif mes == "07":
    mes_extenso = "julho"
elif mes == "08":
    mes_extenso = "agosto"
elif mes == "09":
    mes_extenso = "setembro"
elif mes == "10":
    mes_extenso = "outubro"
elif mes == "11":
    mes_extenso = "novembro"
elif mes == "12":
    mes_extenso = "dezembro"
else:
    mes_extenso = "inválido"

print("Você nasceu em", dia, "de", mes_extenso, "de", ano)
