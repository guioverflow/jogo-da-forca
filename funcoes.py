# Esse arquivo existe a fim de deixar a main mais limpa
# Aqui há as funções que são implementadas na main

from random import randint
from os import system

# Escolhe uma palavra aleatoriamente dentro do documento
def escolher_palavra(documento):
    with open(documento, 'r') as f:
        string = f.read()
        string = string.split('\n')

    # Define uma linha aleatoriamente dentro do documento "vocabulario.txt"
    palavra = string[randint(0, len(string)-1)]

    return palavra

# Faz o display das letras encontradas e não encontradas (P _ l a v r a)
def display_letras(palavra, palavra_bool):
    print('')
    for idx, letra in enumerate(palavra):
        if palavra_bool[idx] == 0:
            print('_', end='')
        elif palavra_bool[idx] == 1:
            print(letra, end='')

def mensagem_final(palavra, vidas):
    system('cls')
    print('A palavra era ' + palavra)
    if (vidas > 0):
        print('Parabéns, você ganhou.\n')
    else:
        print('Você perdeu, mais sorte na próxima.\n')