import csv
from claseViajeroFrecuente import ViajeroFrecuente

def test():
    objetoPrueba = ViajeroFrecuente(1, 1452143214, 'Lucas', 'Avila', 500)
    print(objetoPrueba)

def mostrarDireccionesMemoria(lista):
    for i in range(4):
        print(f'Direccion :{hex(id(lista[i]))} Viajero: {lista[i]}')

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
    test()
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
    band = False
    while i <  len(listaViajeros) and not band:
        if int(listaViajeros[i].getNumero()) == num:
            band = True
        else: 
            i += 1
    
    if i < len(listaViajeros):
        menu(listaViajeros[i])
    else:
        print('No se encontro el numero')

    mostrarDireccionesMemoria(listaViajeros)