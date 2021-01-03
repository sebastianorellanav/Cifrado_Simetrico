import re
from unicodedata import normalize
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encriptar(llave, texto):
    print('Encriptando texto ...')

    #Fase 1: Transposicion
    matriz = []
    for i in range(1,9):
        matriz.append([])
    print(matriz)

    i = 0
    for caracter in texto:
        matriz[i].append(caracter)
        i += 1
        if(i == 8):
            i = 0
    print(matriz)

    encriptado = ''
    for digito in llave:
        for caracter in matriz[digito-1]:
            encriptado = encriptado + caracter

    print(encriptado)


    #Fase 2: Shift

    return ''

def desencriptar(llave, textoEncriptado):
    print('Desencriptando texto ...')

    return ''

def preprocesameientoDeTexto(texto):
    print('Procesando texto ...')
    texto = texto.replace('\n', '')
    # -> NFD y eliminar diacríticos
    texto = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", texto), 0, re.I)
    # -> NFC
    texto = normalize( 'NFC', texto)

    texto = texto.replace('ñ','n').replace('.', '').replace(':','')
    texto = texto.lower()
    print('texto procesado: '+ texto)

    return texto


if __name__ == "__main__":
    llaveSecreta = [1,2,3,4,5,6,7,8]
    texto =  'hola mi nómbre\n es juan'
    textoProcesado = preprocesameientoDeTexto(texto)
    textoEncriptado = encriptar(llaveSecreta, textoProcesado)
    textoDesencriptado = desencriptar(llaveSecreta, textoEncriptado)