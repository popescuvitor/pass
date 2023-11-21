import random
import string

def shuffle_words(frase):
    palavras = frase.split()
    random.shuffle(palavras)
    return ' '.join(palavras)

def generate_password(frase):
    # Alterando a ordem das palavras aleatoriamente
    frase = shuffle_words(frase)

    # Definindo as substituições possíveis
    substitutions = {'a': ['@', '7'], 'b': ['6'],'z': ['2'], 'i': ['!'], 'o': ['0'], 's': ['$'], ' ': ['#', '%', '*', ';', '.', ',', '+', '-']}

    # Convertendo a frase para uma lista de caracteres
    caracteres = list(frase)

    # Aplicando substituições aleatórias
    for i in range(len(caracteres)):
        if caracteres[i].lower() in substitutions and random.choice([True, False]):
            caracteres[i] = random.choice(substitutions[caracteres[i].lower()])

    # Calculando o número de posições onde serão adicionados caracteres aleatórios
    num_caracteres_aleatorios = int(len(caracteres) * 0.2)

    # Escolhendo aleatoriamente as posições onde serão adicionados caracteres aleatórios
    posicoes_aleatorias = random.sample(range(len(caracteres)), num_caracteres_aleatorios)

    # Adicionando caracteres aleatórios nas posições escolhidas
    for i in posicoes_aleatorias:
        caracteres.insert(i, random.choice(string.ascii_letters + string.digits + string.punctuation))

    # Mudando aleatoriamente o case
    for i in range(len(caracteres)):
        if random.choice([True, False]):
            caracteres[i] = caracteres[i].upper()

    # Convertendo a lista de caracteres de volta para uma string
    senha = ''.join(caracteres)
    senha = senha.replace(" ", "").replace("/","\\").replace("|","~").replace("&","`")
    return senha

# Exemplo de uso
frase = input("Digite a frase: ")
for i in range(10):
    senha = generate_password(frase)
    print("Senha gerada:", senha)
