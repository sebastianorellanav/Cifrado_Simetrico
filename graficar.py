import matplotlib.pyplot as plt
import numpy as np

def graficar(x, y1, y2, y3, titulo, xlabel, ylabel, legenda1, legenda2, legenda3):
    plt.figure(figsize=(10,4))
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x,y1, label=legenda1)
    plt.plot(x,y2, label=legenda2)
    plt.plot(x,y3, label=legenda3)
    plt.grid()
    plt.legend(loc="upper right")
    plt.savefig("Resultados/"+titulo+".png")


def graficarResultados(tamanos, tiempoEncPequeño, tiempoEncMediano, tiempoEncLargo, tiempoDesPequeño, tiempoDesMediano, tiempoDesLargo):
    graficar(tamanos,
                                tiempoEncPequeño,
                                tiempoEncMediano,
                                tiempoEncLargo,
                                "Tiempo de Encriptación",
                                "Tamaño de bloque (bits)",
                                "Tiempo (seg)",
                                "texto 4KB",
                                "texto 8KB",
                                "texto 16KB")

    graficar(tamanos,
                                tiempoDesPequeño,
                                tiempoDesMediano,
                                tiempoDesLargo,
                                "Tiempo de Desencriptación",
                                "Tamaño de bloque (bits)",
                                "Tiempo (seg)",
                                "texto 4KB",
                                "texto 8KB",
                                "texto 16KB")
    
    graficar(np.array(tamanos),
                                np.array(tamanos)/np.array(tiempoEncPequeño),
                                np.array(tamanos)/np.array(tiempoEncMediano),
                                np.array(tamanos)/np.array(tiempoEncLargo),
                                "Throughput de Encriptación",
                                "Tamaño de bloque (bits)",
                                "Throughput (bits/seg)",
                                "texto 4KB",
                                "texto 8KB",
                                "texto 16KB")
    
    graficar(np.array(tamanos),
                                np.array(tamanos)/np.array(tiempoDesPequeño),
                                np.array(tamanos)/np.array(tiempoDesMediano),
                                np.array(tamanos)/np.array(tiempoDesLargo),
                                "Throughput de Desencriptación",
                                "Tamaño de bloque (bits)",
                                "Throughput (bits/seg)",
                                "texto 4KB",
                                "texto 8KB",
                                "texto 16KB")

def mostrarResultados():
    plt.show()