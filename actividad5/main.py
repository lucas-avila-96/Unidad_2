from ClaseMenu import Menu
from ClaseManejador import ManejadorPlanes

if __name__ == '__main__':

    ml = ManejadorPlanes()
    ml.testPlanes()
    print('lista de planes inicial')
    print(ml)

    print('1 - Actualizar valor del vehiculo')
    print('2 - Consultar vehiculos con valor de cuota menor que:')
    print('3 - Mostrar monto a pagar para licitar')
    print('4 - Modificar cantidad de cuotas para licitar')

    opcion = int(input('Opcion: '))

    menu = Menu(opcion, ml)