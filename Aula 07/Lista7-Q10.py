def conta_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for letra in palavra:
        if letra in vogais:
            count += 1

    return count

resultado = conta_vogais("python")
print(resultado)  
