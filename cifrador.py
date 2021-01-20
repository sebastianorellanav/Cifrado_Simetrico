import hashlib
import numpy 
import time
import graficar
import conversion
import archivo
import keys 

TAMANO_BLOQUE = 128
RONDAS = 7
subkey = []

# Funcion que implementa un cifrador Fesitel
# Entrada:  textoPanoBinario -> Lista de bits que representan el texto a cifrar
#           F                -> Función F de prueba que se utiliza en el algoritmo de cifrado
#           K1               -> Llave de prueba para la ronda 1 del algoritmo
#           des              -> Booleano que indica si se va a cifrar o descifrar   
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
    return resultado

# Función que genera un a subllave a partir de una llave K
# Luego, se utilizan cada subllave creada para encriptar
# Entrada:  K         -> Lista de bits que representan la llave
#           bloque    -> Lista de bits que representan el bloque
#          
# 
# Salida:   key        -> Lista de bits que representan a la subllave.
def generarSubLlave(K, bloque):
    s = ""
    i = 0
    for b in bloque:
        s += str(bloque[i])
        s += str(K[i])
        i +=1
 
    key = conversion.hexadecimalToBits(hashlib.sha1(s.encode('UTF-8')).hexdigest())
    return key[:(TAMANO_BLOQUE//2)]

# Función que realiza una suma binaria entre dos listas de bits.
# Entrada:  bloque1   -> Lista de bits que representan la mitad de un bloque
#           bloque2   -> Lista de bits que representan la llave de entrada
#          
# 
# Salida:   Resultado  -> Lista de bits resultantes tras la suma binaria
def sumaBloques(bloque1, bloque2):
    resultado = []
    for e1,e2 in zip(bloque1, bloque2):
        e = e1+e2
        if(e > 1):
            e = 0
        resultado.append(e) 

    return resultado

# Función encargada de cifrar un mensaje a partir de una llave inicial.
# El mensaje de entrada es transformado a bits, donde se cifra por cada
# bloque definido. Cada bloque cifrado es concatenado entre sí, para así
# generar el texto completo cifrado.
# Entrada:  mensaje   -> String que representa el mensaje obtenido de un archivo txt
#           K         -> Secuencia de bits que representa la llave inicial. Es definida en código.
#          
# 
# Salida:   textoCifrado   -> Lista de bits que representa al texto cifrado
#           tiempo         -> Tiempo de ejecución del bloque
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

# Función encargada de descifrar un mensaje a partir de una llave inicial.
# El mensaje de entrada es transformado a bits, donde se cifra por cada
# bloque definido. Cada bloque cifrado es concatenado entre sí, para así
# generar el texto completo cifrado.
# Entrada:  mensaje   -> String que representa el mensaje obtenido de un archivo txt
#           K         -> Secuencia de bits que representa la llave inicial. Es definida en código.
#          
# 
# Salida:   textoCifrado   -> Lista de bits que representa al texto cifrado
#           tiempo         -> Tiempo de ejecución del bloque
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

    return textoDescifrado, tiempo



# Función que cálcula el porcentaje de bits diferentes entre una lista y otra.
# Entrada:  bitsCifrados1   -> Lista de bits cifrados originales
#           bitsCifrados2   -> Lista de bits cifrado con un bit diferente a los originales
#          
# 
# Salida:   Porcentaje     -> Porcentaje de bits diferentes entre ambas listas

def efectoAvalancha(bitsCifrados1, bitsCifrados2):
    contador = 0
    for b1, b2 in zip(bitsCifrados1, bitsCifrados2):
        if(b1 != b2):
            contador += 1

    return (contador*100)/len(bitsCifrados1)


# Función que realiza el test avalancha para cada archivo de entrada.
# Entrada: -            
#          
# Salida: -   
def testAvalancha():
    mensaje = archivo.leerArchivo("Texto_Plano_1.txt")
    global subkey
    mod = TAMANO_BLOQUE - (len(mensaje)%TAMANO_BLOQUE)
    for i in range(0, mod):
        mensaje += " "
    
    keyword = "secret"
    K = keys.generarLlave(keyword, int(TAMANO_BLOQUE))

    #cifrar primer texto
    textoCifrado1, tiempo = cifrarTexto(mensaje, K)
    aux = keys.revertirSubkeys(subkey)
    subkey = aux
    textoDescifrado, tiempo = descifrarTexto(textoCifrado1, K)
    print("\n\n")

    #Cifrar segundo texto
    mensaje = archivo.leerArchivo("Texto_Plano_2.txt")
    mod = TAMANO_BLOQUE - (len(mensaje)%TAMANO_BLOQUE)
    for i in range(0, mod):
        mensaje += " "
    subkey = []
    textoCifrado2, tiempo = cifrarTexto(mensaje, K)
    aux = keys.revertirSubkeys(subkey)
    subkey = aux
    textoDescifrado, tiempo = descifrarTexto(textoCifrado2, K)
    
    subkey = []

    #Efecto Avalancha
    avalanchabits = efectoAvalancha(conversion.stringABits(textoCifrado1), conversion.stringABits(textoCifrado2))
    avalanchatexto = efectoAvalancha(textoCifrado1, textoCifrado2)
    print("\n\n==========================================================\nResultado del Test: \n")
    print("Efecto avalancha (% bits diferentes): "+str(avalanchabits))
    print("Efecto avalancha (% caracteres diferentes): "+str(avalanchatexto))

# Función que realiza el test de Throughput para un archivo de entrada
# Entrada:  nombreArchivo  -> Nombre del archivo de entrada representado como un strign
#
# Salida:   
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
        print("\n\n==================================================")
        print("TAMAÑO DE BLOQUE = "+str(t))
        print("\n")
        mod = TAMANO_BLOQUE - (len(mensaje)%TAMANO_BLOQUE)
        for i in range(0, mod):
            mensaje += " "
    
        keyword = "secret"
        K = keys.generarLlave(keyword, int(TAMANO_BLOQUE))
    
        #cifrar 
        textoCifrado1, tiempo = cifrarTexto(mensaje, K)
        tiemposEnc.append(tiempo)
        throughputEnc.append(TAMANO_BLOQUE/tiempo)
        print("\nThroughput Cifrado= "+str(TAMANO_BLOQUE/tiempo))
        print("\n")

        #descifrar
        aux = keys.revertirSubkeys(subkey)
        subkey = aux
        textoDescifrado, tiempo = descifrarTexto(textoCifrado1, K)
        tiemposDes.append(tiempo)
        throughputDes.append(TAMANO_BLOQUE/tiempo)
        subkey = []
        print("\nThroughput Descifrado= "+str(TAMANO_BLOQUE/tiempo))
        
    return tiemposEnc, tiemposDes
            

if __name__ == "__main__":
    print("Bienvenide, ¿Que test desea correr?\n\n")

    print("1. Test Efecto Avalancha")
    print("2. Test Throughput ")

    
    op=0
    
    try:
        op = int(input("Ingrese el numero del test: "))
    except Exception as e:
        while(op!=1 and op!=2 ):
            try:
                print("Opción inválida")
                op = int(input("Ingrese el numero del test nuevamente: "))
            except Exception as identifier:
                pass
    
    if(op==1):
        testAvalancha()
    
    elif(op==2):
        tamanos = [4,8,16,32,64,128]
        tiempoEncPequeño, tiempoDesPequeño = testThroughput("Texto Corto.txt")
        tiempoEncMediano, tiempoDesMediano = testThroughput("Texto Mediano.txt")
        tiempoEncLargo, tiempoDesLargo = testThroughput("Texto Largo.txt")

        graficar.graficarResultados(tamanos, tiempoEncPequeño, tiempoEncMediano, tiempoEncLargo, tiempoDesPequeño, tiempoDesMediano, tiempoDesLargo)

        graficar.mostrarResultados()
    
    else:
        print("Tuviste tu oportunidad y la desaprovechaste, adiós.")

