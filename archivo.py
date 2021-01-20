# Funcion que lee un archivo txt con un nombre definido
# Entrada:  nombre           -> Nombre del archivo representado como un string
# 
# Salida:   texto            -> Texto presente dentro del archivo representado como un string
def leerArchivo(nombre):
    f = open (nombre,'r', encoding="utf8")
    texto = f.read()
    return texto