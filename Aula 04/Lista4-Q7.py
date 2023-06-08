import random

# Lista de palavras
palavras = ['python', 'programacao', 'computador', 'jogo', 'internet']

# Escolhendo uma palavra aleatoriamente
palavra_aleatoria = random.choice(palavras)

# Embaralhando a palavra
letras_embaralhadas = random.sample(palavra_aleatoria, len(palavra_aleatoria))
palavra_embaralhada = ''.join(letras_embaralhadas)

# Número de tentativas
tentativas = 3

# Loop principal do jogo
while tentativas > 0:
    print("Palavra embaralhada:", palavra_embaralhada)
    resposta = input("Digite sua resposta: ")

    # Verificando se a resposta está correta
    if resposta == palavra_aleatoria:
        print("Parabéns! Você acertou a palavra!")
        break
    else:
        print("Resposta incorreta!")
        tentativas -= 1
        print("Tentativas restantes:", tentativas)
        print()

# Mostrando a palavra correta
print("A palavra correta era:", palavra_aleatoria)

# Verificando se o jogador perdeu o jogo
if tentativas == 0:
    print("Você perdeu! Tente novamente.")
