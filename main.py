import hashlib
import numpy 

TAMANO_BLOQUE = 4
RONDAS = 8
subkey = []
#mensaje = "hola a todos"

mensaje = "Mil y una historia me he inventado \nPara estar aquí, aquí a tu lado\nY no te das cuenta que\nYo no encuentro ya qué hacer"\
        "\nSé que piensas que no he sido sincero\nSé que piensas que ya no tengo remedio\n¿Pero quién me iba a decir que sin ti no sé vivir?"\
        "\nY ahora que no estás aquí\nMe doy cuenta cuánta falta me haces\nSi te he fallado, te pido perdón\nDe la única forma que sé"\
        "\nAbriendo las puertas de mi corazón\nPara cuando decidas volver.\n"

"""
mensaje = "Ahí va el Capitán Beto por el espacio\nCon su nave de fibra hecha en Haedo\nAyer colectivero\nHoy amo entre los amos del aire"\
        "\nYa lleva 15 años en su periplo\nSu equipo es tan precario como su destino\nSin embargo, un anillo extraño\nAhuyenta sus peligros en el cosmos"\
        "\nAhí va el Capitán Beto por el espacio\nLa foto de Carlitos sobre el comando\nY un banderín de River Plate\nY la triste estampita de un santo"\
        "\n¿Dónde está el lugar al que todos llaman cielo?\nSi nadie viene hasta aquí a cebarme unos amargos, como en mi viejo umbral"\
        "\n¿Por qué habré venido hasta aquí, si no puedo más de soledad?\nYa no puedo más de soledad\nSu anillo lo inmuniza en los peligros"\
        "\nPero no lo protege de la tristeza\nSurcando la galaxia del Hombre\nAhí va el Capitán Beto, el errante\n¿Dónde habrá una ciudad en la que alguien silbe un tango?"\
        "\n¿Dónde están, dónde están los camiones de basura, mi vieja y el café?\nSi esto sigue así como así, ni una triste sombra quedará"\
        "\nNi una triste sombra quedará\nNi una triste sombra quedará\nAhí va el Capitán Beto por el espacio\nRegando los malvones de su cabina"\
        "\nSin brújula y sin radio\nJamás podrá volver a la Tierra\nTardaron muchos años hasta encontrarlo\nEl anillo de Beto llevaba inscripto un signo del alma  ..."\
        "\n\nAhí va el Capitán Beto por el espacio\nCon su nave de fibra hecha en Haedo\nAyer colectivero\nHoy amo entre los amos del aire"\
        "\nYa lleva 15 años en su periplo\nSu equipo es tan precario como su destino\nSin embargo, un anillo extraño\nAhuyenta sus peligros en el cosmos"\
        "\nAhí va el Capitán Beto por el espacio\nLa foto de Carlitos sobre el comando\nY un banderín de River Plate\nY la triste estampita de un santo"\
        "\n¿Dónde está el lugar al que todos llaman cielo?\nSi nadie viene hasta aquí a cebarme unos amargos, como en mi viejo umbral"\
        "\n¿Por qué habré venido hasta aquí, si no puedo más de soledad?\nYa no puedo más de soledad\nSu anillo lo inmuniza en los peligros"\
        "\nPero no lo protege de la tristeza\nSurcando la galaxia del Hombre\nAhí va el Capitán Beto, el errante\n¿Dónde habrá una ciudad en la que alguien silbe un tango?"\
        "\n¿Dónde están, dónde están los camiones de basura, mi vieja y el café?\nSi esto sigue así como así, ni una triste sombra quedará"\
        "\nNi una triste sombra quedará\nNi una triste sombra quedará\nAhí va el Capitán Beto por el espacio\nRegando los malvones de su cabina"\
        "\nSin brújula y sin radio\nJamás podrá volver a la Tierra\nTardaron muchos años hasta encontrarlo\nEl anillo de Beto llevaba inscripto un signo del alma  ..."\
        "\n\nAhí va el Capitán Beto por el espacio\nCon su nave de fibra hecha en Haedo\nAyer colectivero\nHoy amo entre los amos del aire"\
        "\nYa lleva 15 años en su periplo\nSu equipo es tan precario como su destino\nSin embargo, un anillo extraño\nAhuyenta sus peligros en el cosmos"\
        "\nAhí va el Capitán Beto por el espacio\nLa foto de Carlitos sobre el comando\nY un banderín de River Plate\nY la triste estampita de un santo"\
        "\n¿Dónde está el lugar al que todos llaman cielo?\nSi nadie viene hasta aquí a cebarme unos amargos, como en mi viejo umbral"\
        "\n¿Por qué habré venido hasta aquí, si no puedo más de soledad?\nYa no puedo más de soledad\nSu anillo lo inmuniza en los peligros"\
        "\nPero no lo protege de la tristeza\nSurcando la galaxia del Hombre\nAhí va el Capitán Beto, el errante\n¿Dónde habrá una ciudad en la que alguien silbe un tango?"\
        "\n¿Dónde están, dónde están los camiones de basura, mi vieja y el café?\nSi esto sigue así como así, ni una triste sombra quedará"\
        "\nNi una triste sombra quedará\nNi una triste sombra quedará\nAhí va el Capitán Beto por el espacio\nRegando los malvones de su cabina"\
        "\nSin brújula y sin radio\nJamás podrá volver a la Tierra\nTardaron muchos años hasta encontrarlo\nEl anillo de Beto llevaba inscripto un signo del alma  ..."\
        "\n\nAhí va el Capitán Beto por el espacio\nCon su nave de fibra hecha en Haedo\nAyer colectivero\nHoy amo entre los amos del aire"\
        "\nYa lleva 15 años en su periplo\nSu equipo es tan precario como su destino\nSin embargo, un anillo extraño\nAhuyenta sus peligros en el cosmos"\
        "\nAhí va el Capitán Beto por el espacio\nLa foto de Carlitos sobre el comando\nY un banderín de River Plate\nY la triste estampita de un santo"\
        "\n¿Dónde está el lugar al que todos llaman cielo?\nSi nadie viene hasta aquí a cebarme unos amargos, como en mi viejo umbral"\
        "\n¿Por qué habré venido hasta aquí, si no puedo más de soledad?\nYa no puedo más de soledad\nSu anillo lo inmuniza en los peligros"\
        "\nPero no lo protege de la tristeza\nSurcando la galaxia del Hombre\nAhí va el Capitán Beto, el errante\n¿Dónde habrá una ciudad en la que alguien silbe un tango?"\
        "\n¿Dónde están, dónde están los camiones de basura, mi vieja y el café?\nSi esto sigue así como así, ni una triste sombra quedará"\
        "\nNi una triste sombra quedará\nNi una triste sombra quedará\nAhí va el Capitán Beto por el espacio\nRegando los malvones de su cabina"\
        "\nSin brújula y sin radio\nJamás podrá volver a la Tierra\nTardaron muchos años hasta encontrarlo\nEl anillo de Beto llevaba inscripto un signo del alma"
"""

# Funcion que permite convertir una lista de bits a un String
# Entrada:  bits      -> Lista de bits a convertir
# 
# Salida:   resultado -> String convertido
def bitsAString(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


# Funcion que permite convertir un string a una lista de Bits
# Entrada:  s         -> String a convertir
# 
# Salida:   resultado -> Lista de bits que representan el string
def stringABits(s):
    resultado = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        resultado.extend([int(b) for b in bits])
    
    return resultado


def generarSubLlave(K, bloque):
    s = ""
    for i in bloque:
        s += str(bloque[i])
        s += str(K[i])
 
    key = hexadecimalToBits(hashlib.sha1(s.encode('UTF-8')).hexdigest())
    return key[:(TAMANO_BLOQUE//2)]


# Funcion que implementa un cifrador Fesitel
# Entrada:  textoPanoBinario -> Lista de bits que representan el texto a cifrar
#           F                -> Función F de prueba que se utiliza en el algoritmo de cifrado
#           K1               -> Llave de prueba para la ronda 1 del algoritmo
# 
# Salida:   binarioCifrado   -> Lista de bits que representan el texto cifrado 
def cifradorFeistel(textoPlanoBinario, F, K, des):
    LE0 = textoPlanoBinario[0:int(TAMANO_BLOQUE/2)]
    RE0 = textoPlanoBinario[int(TAMANO_BLOQUE/2): ]

    for ronda in range(0, RONDAS):
        if(des):
            subK = subkey[ronda]
        else:
            subK = generarSubLlave(K, LE0)
            subkey.append(subK)
        
        resultadoF = F(RE0, subK)
        RE1 = XOR(LE0, resultadoF)

        # Se forma el bloque para la siguiente iteración
        LE0 = RE0
        RE0 = RE1

    # luego de las rondas se invierten los bloques
    binarioCifrado = RE0 + LE0

    return binarioCifrado


# Funcion que implementa una compuerta lógica XOR u OR-exclusivo
# Entrada:  bloque1   -> Lista de bits que representan el primer bloque
#           bloque2   -> Lista de bits que representan el segundo bloque
# 
# Salida:   resultado -> Lista de bits que representan el resultado de la compuerta XOR
def XOR(bloque1, bloque2):
    resultado = []
    for b1,b2 in zip(bloque1, bloque2):
        if(b1 == b2):
            resultado.append(0)
        elif((b1 == 0 and b2 == 1) or (b1 == 1 and b2 == 0)):
            resultado.append(1)
    
    return resultado


# Funcion que implementa la función F de prueba para ser utilizada en el algoritmo de cifrado Feistel
# esta función coloca un bit de la llave si la posicion es par o un bit del bloque si es impar
# Entrada:  bloque    -> Lista de bits que representan el bloque
#           llave     -> Lista de bits que representan la llave
# 
# Salida:   resultado -> Lista de bits que representan el resultado de la función F
def F(mitadBloque, llave):
    resultado = []

    mitadBloque = mitadBloque[::-1]
    resultado = sumaBloques(mitadBloque, llave)
    
    llave = XOR(llave, llave)

    for i in range(0, len(resultado)):
        if(resultado[i] == 0):
            resultado[i] = 1
        else:
            resultado[i] = 0
    
    resultado = sumaBloques(resultado, llave)
    
    return resultado

def sumaBloques(bloque1, bloque2):
    resultado = []
    for e1,e2 in zip(bloque1, bloque2):
        e = e1+e2
        if(e > 1):
            e = 0
        resultado.append(e) 

    return resultado

def cifrarTexto(K):
    mensajeBits = stringABits(mensaje)
    cantidadBloques = int(len(mensajeBits)/TAMANO_BLOQUE)

    print("Texto Original: "+mensaje)
    #print("Bits Texto Original: "+str(mensajeBits))
    print("\n\n")

    ######################################################
    # Cifrar
    #########
    print("Cifrando Texto ...")
    i = 0
    bitsCifrados = []
    for numeroBloque in range(0, int(cantidadBloques)):
        
        bloque = mensajeBits[i:(TAMANO_BLOQUE)+i]
        bloqueCifrado = cifradorFeistel(bloque, F, K, False)
        bitsCifrados += bloqueCifrado
        i += (TAMANO_BLOQUE)
    
    textoCifrado = bitsAString(bitsCifrados)
    print("Texto Cifrado: "+textoCifrado)
    #print("Bits Texto Cifrado: "+ str(bitsCifrados))
    print("\n\n")
    
    return textoCifrado


def descifrarTexto(textoCifrado):
    global subkey 
    bitsCifrados = stringABits(textoCifrado)
    cantidadBloques = int(len(bitsCifrados)/TAMANO_BLOQUE)
    print("Descifrando Texto ...")
    i = 0
    bitsDescifrados = []
    for numeroBloque in range(0, int(cantidadBloques)):
        bloque = bitsCifrados[i: (TAMANO_BLOQUE)+i]
        bloqueDescifrado = cifradorFeistel(bloque, F, K, True)
        bitsDescifrados += bloqueDescifrado
        subkey = subkey[RONDAS:]
        i += (TAMANO_BLOQUE)
    
    textoDescifrado = bitsAString(bitsDescifrados)
    print("Texto Descifrado: "+textoDescifrado)
    #print("Bits Texto Descifrado: "+ str(bitsDescifrados))

    return textoDescifrado

def generarLlave(keyword, tamañoLLave):
    h = hashlib.md5()
    h.update(keyword.encode('UTF-8'))
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    key = []
    aux = list(bin(int(h.hexdigest(), scale))[2:].zfill(num_of_bits))
    j = 0
    for i in range(0,tamañoLLave):
        if (j == len(aux)):
            j = 0
        key.append( int( aux[j] ) )
        j +=1
    return key

def hexadecimalToBits(stringHex):
    res = "{0:08b}".format(int(stringHex, 16)) 
    res = [int(b) for b in list(res)]
    return res

def revertirSubkeys(keys):
    skaux = []
    i = 0
    for v in range(0, len(keys)//RONDAS):
        aux = keys[i: i+RONDAS]
        aux = aux[::-1]
        skaux.extend(aux)
        i += RONDAS
    return skaux

def efectoAvalancha(bitsCifrados1, bitsCifrados2):
    contador = 0
    for b1, b2 in zip(bitsCifrados1, bitsCifrados2):
        if(b1 != b2):
            contador += 1

    return (contador/len(bitsCifrados1))*100

if __name__ == "__main__":
    mod = TAMANO_BLOQUE - (len(mensaje)%TAMANO_BLOQUE)
    for i in range(0, mod):
        mensaje += " "
    
    keyword = "secreto"
    K = generarLlave(keyword, int(TAMANO_BLOQUE))
    print(K)

    textoCifrado1 = cifrarTexto(K)
    mensaje = "Ail y una historia me he inventado \nPara estar aquí, aquí a tu lado\nY no te das cuenta que\nYo no encuentro ya qué hacer"\
        "\nSé que piensas que no he sido sincero\nSé que piensas que ya no tengo remedio\n¿Pero quién me iba a decir que sin ti no sé vivir?"\
        "\nY ahora que no estás aquí\nMe doy cuenta cuánta falta me haces\nSi te he fallado, te pido perdón\nDe la única forma que sé"\
        "\nAbriendo las puertas de mi corazón\nPara cuando decidas volver.\n"

    textoCifrado2 = cifrarTexto(K)
    avalancha = efectoAvalancha(stringABits(textoCifrado1), stringABits(textoCifrado2))
    print("Efecto avalancha: "+str(avalancha))

    aux = revertirSubkeys(subkey)
    subkey = aux
    textoDescifrado = descifrarTexto(textoCifrado1)




















































































































"""
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


def avalancheTest(message1,message2,key):
    m1 = message1
    bitsm1 = ' '.join(format(x, 'b') for x in bytearray(m1, 'utf-8'))
    m2 = message2
    bitsm2 = ' '.join(format(x, 'b') for x in bytearray(m2, 'utf-8'))
    #For the first message, example: "hola"
    textoProcesado1 = preprocesameientoDeTexto(m1)
    textoEncriptado1 = encriptar(llaveSecreta, textoProcesado1)
    out1 = ' '.join(format(x, 'b') for x in bytearray(textoEncriptado1, 'utf-8'))
    print("La palabra "+m1+" encriptada con llave "+str(key)+" tiene como resultado "+textoEncriptado1+", cuyos bits son: "+str(out1))
    #For the second message, example: "hole"
    textoProcesado2 = preprocesameientoDeTexto(m2)
    textoEncriptado2 = encriptar(llaveSecreta, textoProcesado2)
    out2 = ' '.join(format(x, 'b') for x in bytearray(textoEncriptado2, 'utf-8'))
    print("La palabra "+m2+" encriptada con llave "+str(key)+" tiene como resultado "+textoEncriptado2+", cuyos bits son: "+str(out2))

if __name__ == "__main__":
    llaveSecreta = [4,3,1,2,5,6,7,8]
    texto1 =  'hola como estas'
    texto2 =  'hole como estas'
    avalancheTest(texto1, texto2, llaveSecreta)

    #textoProcesado = preprocesameientoDeTexto(texto)
    #textoEncriptado = encriptar(llaveSecreta, textoProcesado)
    #textoDesencriptado = desencriptar(llaveSecreta, textoEncriptado)

"""