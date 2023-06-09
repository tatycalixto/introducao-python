def somaImposto(taxaImposto,custo):
    custo_total = (custo*taxaImposto)/100
    custo_total +=custo 
    print (custo_total)

somaImposto(50,100)