from variaveis import *
from funcoes import *
from os import system

def game(palavra, palavra_bool, vidas, letras_tentadas, letra_input):
    # "vocabulario.txt" é o arquivo que contém uma coleção de palavras
    # Fonte: http://hackingportuguese.com/sample-page/the-1000-most-common-nouns-in-portuguese/
    palavra = escolher_palavra('vocabulario.txt')

    # Mapeamento de adivinhações da palavra, todas as letras começam como "0"
    palavra_bool = [0 for letra in palavra]

    # O jogo vai rolar enquanto o jogador tem vidas, ou enquanto a palavra não foi totalmente adivinhada
    while(vidas > 0 and (0 in palavra_bool)):
        system('cls')
        print('Vidas: ', vidas)
        print('Letras tentadas: ', end='')
        
        # Printa as letras tentadas
        for letra in letras_tentadas:
            print(letra, ' ', end='')

        display_letras(palavra, palavra_bool)
        
        # Input do usuário
        letra_input = input('\n\nDigite uma letra: ')

        # Sair do jogo
        if letra_input.isdigit():
            if int(letra_input) == 0:
                return

        # Validação do input; verifica se já foi tentada, se é um caracter e se foi digitada apenas uma letra
        if (letra_input in letras_tentadas) or not letra_input.isalpha() or len(letra_input) != 1:
            continue
        else:
            letras_tentadas.append(letra_input)
            letras_tentadas.sort()
        
        # Procede com a atualização do mapeamento caso o usário tenha acertado
        # Ou com a retirada da vida caso o usuário tenha errado
        if letra_input in palavra:
            for idx, letra in enumerate(palavra):
                if letra == letra_input:
                    palavra_bool[idx] = 1
        else:
            vidas -= 1
        
    mensagem_final(palavra, vidas)

if __name__ == '__main__':
    print('Bem-vindo ao jogo da forca.')
    print('O objetivo é adivinhar a palavra, você terá cinco vidas e a cada erro será subtraída uma.')
    print('Caso queira finalizar o jogo pressione 0 a qualquer momento.\n')
    print('Nota: Palavras com cedilha serão escritas apenas como "c".\n')
    print('Pressione ENTER para começar.', end='')

    if(input() != '0'):
        game(palavra, palavra_bool, vidas, letras_tentadas, letra_input)