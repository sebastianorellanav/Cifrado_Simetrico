def leerArchivo(nombre):
    f = open (nombre,'r', encoding="utf8")
    texto = f.read()
    return texto