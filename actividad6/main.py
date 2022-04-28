import csv
from claseViajeroFrecuente import ViajeroFrecuente

if __name__ == '__main__':
    listaViajeros = []
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo, delimiter = ';')
    next(reader)

    for linea in reader:
        listaViajeros.append(ViajeroFrecuente(linea[0], linea[1], linea[2], linea[3], linea[4]))
    
    max_millas = listaViajeros[0]

    for elemento in listaViajeros:
        if elemento > max_millas:
            max_millas = elemento

    for elemento in listaViajeros:
        if(elemento == max_millas):
            print(elemento)
            
    v = ViajeroFrecuente(40,1351235,'lucas', 'avila', 100)

    print('---ACUMULAR MILLAS---')
    v = v + 100
    print(v)
    print('---CANJEAR MILLAS---')
    v = v - 50
    print(v)
