import random

def embaralhar_string(texto):
    texto = texto.lower()
    caracteres = list(texto)
    random.shuffle(caracteres)
    texto_embaralhado = ''.join(caracteres)
    return texto_embaralhado

print(embaralhar_string("Python"))
