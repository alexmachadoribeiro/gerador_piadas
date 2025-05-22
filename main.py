# importa bibliotecas
import pyjokes
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source="auto", target="pt")

while True:
    piada = pyjokes.get_joke() # gera piada
    piada_traduzida = tradutor.translate(piada) # traduz piada

    print(piada_traduzida) # exibe piada traduzida

    repetir = input('Gerar outra piada? "s" para sim; qualquer outro valor para encerrar: ').lower()

    if repetir == 's':
        continue
    else:
        break
