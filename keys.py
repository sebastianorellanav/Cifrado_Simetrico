import hashlib
from cifrador import TAMANO_BLOQUE, RONDAS
import conversion



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