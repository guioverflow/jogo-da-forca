
# Esse código serve para extrair uma lista de palavras do conteúdo bruto do site.
# Fonte das palavras: http://hackingportuguese.com/sample-page/the-1000-most-common-nouns-in-portuguese/

from unidecode import unidecode

with open('1000palavras.txt', 'r', encoding='utf-8') as f:
    lista = f.read()
    lista = lista.split('\n')

for idx, palavra in enumerate(lista):
    primeiro = palavra.find('[') + 1
    segundo = palavra.find(']')
    palavra = palavra[primeiro:segundo]

    if ((index_corrigido := palavra.find(' ')) != -1):
        palavra = palavra[index_corrigido+1:]
    
    lista[idx] = unidecode(palavra)

lista_aux = [palavra for palavra in lista if len(palavra) >= 4]
lista = lista_aux

with open('./../vocabulario.txt', 'w') as f:
    for idx, palavra in enumerate(lista):
        if idx != (len(lista) - 1):
            f.write(palavra + '\n')
        else:
            f.write(palavra)