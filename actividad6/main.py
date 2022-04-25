import csv
from claseViajeroFrecuente import ViajeroFrecuente

def menu(viajero):

    print('Elija una opcion:')
    print('1 - Consultar millas')
    print('2 - Acumular millas')
    print('3 - Canjear millas')

    opcion = int(input('Opcion: '))
    
    match opcion:
        case 1:
            print(f'Cantidad de millas: {viajero.cantidadTotalMillas()}')
        case 2:
            print(f'Acumular millas de millas: {viajero.acumularMillas()}')
        case 3:
            print(f'Canjear millas: {viajero.canjearMillas()}')
        case _:
            print('opcion incorrecta')


if __name__ == '__main__':
    listaViajeros = []
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo, delimiter = ';')
    next(reader)

    for linea in reader:
        listaViajeros.append(ViajeroFrecuente(linea[0], linea[1], linea[2], linea[3], linea[4]))
    
    
    max_millas = max(listaViajeros)

    for elemento in listaViajeros:
        if(elemento == max_millas):
            print(f'Viajero: {elemento.get_nombre()}, Millas: {elemento.cantidadTotalMillas()}')
            
    v = ViajeroFrecuente(40,1351235,'lucas', 'avila', 100)
    v = v + 100

    print(v.cantidadTotalMillas())
    
