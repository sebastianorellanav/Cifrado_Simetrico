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

def hexadecimalToBits(stringHex):
    res = "{0:08b}".format(int(stringHex, 16)) 
    res = [int(b) for b in list(res)]
    return res