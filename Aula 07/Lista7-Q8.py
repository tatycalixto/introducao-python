def maior_numero(lista):
    if len(lista) == 0:
        return None

    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

numeros = [10, 5, 8, 20, 15]
resultado = maior_numero(numeros)
print(resultado)  
