import re
from unicodedata import normalize
import sys 

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encriptar(llave, texto):
    print('Encriptando texto ...')

    #Fase 1: Transposicion
    matriz = []  # se crea la matriz
    
    # Se agregan 7 listas vacias
    for i in range(1,len(llave)+1):
        matriz.append([])
        # a cada lista se le agrega al principio el digito de la llave que corresponda
        matriz[i-1].append(llave[i-1])
    print(matriz)

    i = 0
    # para cada caracter en el texto original
    for caracter in texto:
        # se agrega el caracter a la matriz en orden
        matriz[i].append(caracter)
        i += 1
        if(i == len(llave)):
            i = 0
    print(matriz)

    encriptado = ''
    flag = 0
    # para i desde 1 hasta 7
    for i in range(1,len(llave)+1):
        flag = 0
        # se debe buscar en todas las columnas
        for columna in matriz:
            # si el numero de columna es igual al numero de iteracion
            if (i == columna[0]):
                # se copian los caracteres en el texto cifrado
                for i in range(1,len(columna)):
                    encriptado = encriptado + columna[i]
                flag = 1
            if(flag == 1):
                break

    print(encriptado)

    #Fase 2: Shift
    encriptado2 = ''
    i = 0
    # para cada caracter ya encriptado
    for caracter in encriptado:
        # si el caracter es distinto de un espacio
        if(caracter != ' '):
            # se obtiene un digito de la llave segun posicion i
            # el digito obtenido indica el corrimiento del caracter en el alfabeto
            num_shift = llave[i]
            # se obtiene la posicion del caracter en el alfabeto
            index = alfabeto.index(caracter)
            # se suma la posicion obtenida con el shift correspondiente
            index = index +num_shift
            # se verifica que se está dentro del rango del alfabeto
            if(index >= len(alfabeto)):
                # en caso de que el indice este fuera del rango se vuelve al inicio
                index = index - len(alfabeto)
            # se agrega el caracter encriptado al texto final
            encriptado2 = encriptado2 + alfabeto[index]
            i +=1
        
        # si el caracter es un espacio se deja igual
        else:
            encriptado2 = encriptado2 + ' '
        # si el indice de la llave se sale del rango se vuelve al inicio
        if(i == len(llave)):
            i = 0

    print(encriptado2)
    return encriptado2

def desencriptar(llave, textoEncriptado):
    print('Desencriptando texto ...')

    #Fase 1: correr cada caracter hacia atrás tantas posiciones como indique la llave
    desencriptado1 = ''
    i = 0
    # para cada caracter ya encriptado
    for caracter in textoEncriptado:
        # si el caracter es distinto de un espacio
        if(caracter != ' '):
            # se obtiene un digito de la llave segun posicion i
            # el digito obtenido indica el corrimiento del caracter en el alfabeto
            num_shift = llave[i]
            # se obtiene la posicion del caracter en el alfabeto
            index = alfabeto.index(caracter)
            # se suma la posicion obtenida con el shift correspondiente
            index = index -num_shift
            # se verifica que se está dentro del rango del alfabeto
            if(index < 0):
                # en caso de que el indice este fuera del rango se vuelve al inicio
                index = index + len(alfabeto)
            # se agrega el caracter encriptado al texto final
            desencriptado1 = desencriptado1 + alfabeto[index]
            i +=1
        
        # si el caracter es un espacio se deja igual
        else:
            desencriptado1 = desencriptado1 + ' '
        # si el indice de la llave se sale del rango se vuelve al inicio
        if(i == len(llave)):
            i = 0

    print('fase 1 desencriptacion:')
    print(desencriptado1)

    #Fase 2: 
    tamanoBloque = int(len(desencriptado1)/len(llave))
    matriz = []  # se crea la matriz
    
    # Se agregan 8 listas vacias
    for i in range(1,len(llave)+1):
        matriz.append([])
        # a cada lista se le agrega al principio el digito de la llave que corresponda
        matriz[i-1].append(llave[i-1])
    print(matriz)

    print(tamanoBloque)
    i=0
    for j in range(0, len(llave)):
        bloque = desencriptado1[0+i:tamanoBloque+i]
        print(bloque)
        for columna in matriz:
            if(columna[0] == j+1):
                for caracter in bloque:
                    columna.append(caracter)
                i += tamanoBloque

    print(matriz)

    desencriptado2 = ''
    for i in range(1, tamanoBloque+1):
        for j in range(0, len(llave)):
            desencriptado2 = desencriptado2 + matriz[j][i]

    print(desencriptado2)

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

    # se agregan espacios para que el numero de caracteres sea multiplo de 8
    if(len(texto)%8 != 0):
        texto = texto + ' '*(8 - len(texto)%8)
    return texto


if __name__ == "__main__":
    llaveSecreta = [4,3,1,2,5,6,7,8]
    texto =  'hi hitler salve hitler'
    textoProcesado = preprocesameientoDeTexto(texto)
    textoEncriptado = encriptar(llaveSecreta, textoProcesado)
    textoDesencriptado = desencriptar(llaveSecreta, textoEncriptado)