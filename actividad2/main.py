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
            print(f'Cantidad de millas: {viajero.acumularMillas()}')
        case 3:
            print(f'Cantidad de millas: {viajero.canjearMillas()}')
        case _:
            print('opcion incorrecta')


if __name__ == '__main__':
    listaViajeros = []
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo, delimiter = ';')
    next(archivo, None)

    for linea in reader:
        listaViajeros.append(ViajeroFrecuente(linea[0], linea[1], linea[2], linea[3],))
    
    print('Ingrese numero de viajero: ')
    num = int(input('Numero: '))
    i = 0

    while i <  len(listaViajeros):
        if int(listaViajeros[i].getNumero()) == num:
            break
        else:
            i += 1
    
    if i < len(listaViajeros):
        menu(listaViajeros[i])
    else:
        print('No se encontro el numero')
        
    
