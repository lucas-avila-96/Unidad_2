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
   v1 = ViajeroFrecuente(1, 39425676, 'Lucas', 'Avila', 500)
   v2 = ViajeroFrecuente(2, 40435175, 'Juan', 'Perez', 500)
   print(v1 == v2)
   
   v1 = 500 + v1
   print(v1)

   v2 = v2 - 600
   print(v2)

