# importa bibliotecas
import pyjokes
from googletrans import Translator

tradutor = Translator()

while True:
    piada = pyjokes.get_joke() # gera piada
    piada_traduzida = tradutor.translate(piada, dest='pt') # traduz piada

    print(piada_traduzida.text) # exibe piada traduzida

    repetir = input('Gerar outra piada? "s" para sim; qualquer outro valor para encerrar: ').lower()

    if repetir == 's':
        continue
    else:
        break
