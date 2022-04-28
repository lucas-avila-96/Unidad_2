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
            viajero.cantidadTotalMillas()
        case 2:
            viajero.acumularMillas()
        case 3:
            viajero.canjearMillas()
        case _:
            print('opcion incorrecta')


if __name__ == '__main__':
    listaViajeros = []
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo, delimiter = ';')
    next(reader)

    for linea in reader:
        num = linea[0]
        dni = linea[1]
        nombre = linea[2]
        apellido = linea[3]
        millas = linea[4]
        listaViajeros.append(ViajeroFrecuente(num, dni, nombre, apellido, millas))
    
    print('Ingrese numero de viajero: ')
    num = int(input('Numero: '))
    i = 0

    while i <  len(listaViajeros) and int(listaViajeros[i].getNumero()) != num:
            i += 1
    
    if i < len(listaViajeros):
        menu(listaViajeros[i])
    else:
        print('No se encontro el numero')
