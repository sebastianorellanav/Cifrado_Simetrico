import hashlib
import numpy 
import time
import matplotlib.pyplot as plt
import conversion
import archivo

TAMANO_BLOQUE = 8
RONDAS = 7
subkey = []

def generarSubLlave(K, bloque):
    s = ""
    i = 0
    for b in bloque:
        s += str(bloque[i])
        s += str(K[i])
        i +=1
 
    key = conversion.hexadecimalToBits(hashlib.sha1(s.encode('UTF-8')).hexdigest())
    return key[:(TAMANO_BLOQUE//2)]


# Funcion que implementa un cifrador Fesitel
# Entrada:  textoPanoBinario -> Lista de bits que representan el texto a cifrar
#           F                -> Función F de prueba que se utiliza en el algoritmo de cifrado
#           K1               -> Llave de prueba para la ronda 1 del algoritmo
# 
# Salida:   binarioCifrado   -> Lista de bits que representan el texto cifrado 
def cifradorFeistel(textoPlanoBinario, F, K, des):
    global subkey
    LE0 = textoPlanoBinario[0:int(TAMANO_BLOQUE/2)]
    RE0 = textoPlanoBinario[int(TAMANO_BLOQUE/2): ]

    for ronda in range(0, RONDAS):
        if(des):
            subK = subkey[ronda]
        else:
            if ronda > 0:
                subK = generarSubLlave(subkey[ronda-1], RE0)
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
    

    s = ""
    i = 0
    for b in resultado:
        s += str(resultado[i])
        s += str(llave[i])
        i +=1
 
    key = conversion.hexadecimalToBits(hashlib.sha1(s.encode('UTF-8')).hexdigest())
    key = key[:len(resultado)]

    for i in range(0, len(resultado)-1):
        e = key[i]+llave[i+1]
        if e>1:
            e = 1
        resultado[i] = e
    
    #resultado = sumaBloques(resultado, llave)
    
    return resultado

def sumaBloques(bloque1, bloque2):
    resultado = []
    for e1,e2 in zip(bloque1, bloque2):
        e = e1+e2
        if(e > 1):
            e = 0
        resultado.append(e) 

    return resultado

def cifrarTexto(mensaje, K):
    mensajeBits = conversion.stringABits(mensaje)
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
    inicio = time.time()
    for numeroBloque in range(0, int(cantidadBloques)):
        
        bloque = mensajeBits[i:(TAMANO_BLOQUE)+i]
        bloqueCifrado = cifradorFeistel(bloque, F, K, False)
        bitsCifrados += bloqueCifrado
        i += (TAMANO_BLOQUE)
    
    textoCifrado = conversion.bitsAString(bitsCifrados)
    tiempo = time.time() - inicio
    print("Texto Cifrado: "+textoCifrado)
    #print("Bits Texto Cifrado: "+ str(bitsCifrados))
    print("\n\n")
    
    return textoCifrado, tiempo


def descifrarTexto(textoCifrado, K):
    global subkey 
    bitsCifrados = conversion.stringABits(textoCifrado)
    cantidadBloques = int(len(bitsCifrados)/TAMANO_BLOQUE)
    print("Descifrando Texto ...")
    i = 0
    bitsDescifrados = []
    inicio = time.time()
    for numeroBloque in range(0, int(cantidadBloques)):
        bloque = bitsCifrados[i: (TAMANO_BLOQUE)+i]
        bloqueDescifrado = cifradorFeistel(bloque, F, K, True)
        bitsDescifrados += bloqueDescifrado
        subkey = subkey[RONDAS:]
        i += (TAMANO_BLOQUE)
    
    textoDescifrado = conversion.bitsAString(bitsDescifrados)
    tiempo = time.time() - inicio
    print("Texto Descifrado: "+textoDescifrado)
    #print("Bits Texto Descifrado: "+ str(bitsDescifrados))

    return textoDescifrado, tiempo

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

    return (contador*100)/len(bitsCifrados1)



def testAvalancha():
    mensaje = archivo.leerArchivo("Texto_Plano_1.txt")
    global subkey
    mod = TAMANO_BLOQUE - (len(mensaje)%TAMANO_BLOQUE)
    for i in range(0, mod):
        mensaje += " "
    
    keyword = "secret"
    K = generarLlave(keyword, int(TAMANO_BLOQUE))

    #cifrar primer texto
    textoCifrado1, tiempo = cifrarTexto(mensaje, K)
    aux = revertirSubkeys(subkey)
    subkey = aux
    textoDescifrado, tiempo = descifrarTexto(textoCifrado1, K)
    
    #Cifrar segundo texto
    mensaje = archivo.leerArchivo("Texto_Plano_2.txt")
    mod = TAMANO_BLOQUE - (len(mensaje)%TAMANO_BLOQUE)
    for i in range(0, mod):
        mensaje += " "
    subkey = []
    textoCifrado2, tiempo = cifrarTexto(mensaje, K)
    aux = revertirSubkeys(subkey)
    subkey = aux
    textoDescifrado, tiempo = descifrarTexto(textoCifrado2, K)
    
    subkey = []

    #Efecto Avalancha
    avalancha = efectoAvalancha(conversion.stringABits(textoCifrado1), conversion.stringABits(textoCifrado2))
    print("Efecto avalancha: "+str(avalancha))

def testThroughput(nombreArchivo):
    mensaje = archivo.leerArchivo(nombreArchivo)
    global subkey
    global TAMANO_BLOQUE
    tamanos = [4,8,16,32,64,128]
    tiemposEnc = []
    throughputEnc = []
    tiemposDes = []
    throughputDes = []

    for t in tamanos:
        TAMANO_BLOQUE = t
        mod = TAMANO_BLOQUE - (len(mensaje)%TAMANO_BLOQUE)
        for i in range(0, mod):
            mensaje += " "
    
        keyword = "secret"
        K = generarLlave(keyword, int(TAMANO_BLOQUE))
    
        #cifrar 
        textoCifrado1, tiempo = cifrarTexto(mensaje, K)
        tiemposEnc.append(tiempo)
        throughputEnc.append(TAMANO_BLOQUE/tiempo)
        
        #descifrar
        aux = revertirSubkeys(subkey)
        subkey = aux
        textoDescifrado, tiempo = descifrarTexto(textoCifrado1, K)
        tiemposDes.append(tiempo)
        throughputDes.append(TAMANO_BLOQUE/tiempo)
        subkey = []
    
    plt.figure()
    nombre = "Tiempo de Cifrado de "+nombreArchivo[:len(nombreArchivo)-4]
    plt.title(nombre)
    plt.xlabel("Tamaño de bloque (bits)")
    plt.ylabel("Tiempo (seg)")
    plt.plot(tamanos, tiemposEnc, color='g')
    plt.grid()
    plt.savefig(nombre+".jpeg")

    nombre = "Throughput de Cifrado de "+nombreArchivo[:len(nombreArchivo)-4]
    plt.figure()
    plt.xlabel("Tamaño de bloque (bits)")
    plt.ylabel("Throughput (bits/seg)")
    plt.title(nombre)
    plt.plot(tamanos, throughputEnc, color='r')
    plt.grid()
    plt.savefig(nombre+".jpeg")

    nombre = "Tiempo de Descifrado de "+nombreArchivo[:len(nombreArchivo)-4]
    plt.figure()
    plt.xlabel("Tamaño de bloque (bits)")
    plt.ylabel("Tiempo (seg)")
    plt.title(nombre)
    plt.plot(tamanos, tiemposDes, color='b')
    plt.grid()
    plt.savefig(nombre+".jpeg")
    
    nombre = "Throughput de Descifrado de "+nombreArchivo[:len(nombreArchivo)-4]
    plt.figure()
    plt.xlabel("Tamaño de bloque (bits)")
    plt.ylabel("Throughput (bits/seg)")
    plt.title(nombre)
    plt.plot(tamanos, throughputDes, color='orange')
    plt.grid()
    plt.savefig(nombre+".jpeg")
    plt.show()

    
            

if __name__ == "__main__":
    testAvalancha()

    testThroughput("Texto Pequeño.txt")
    #testThroughput("Texto Mediano.txt")
    #testThroughput("Texto Largo.txt")
