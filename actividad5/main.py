import csv
from clase import PlanAhorro


def actualizar(lista):
    for elemento in lista:
        elemento.mostrar_info()
        nuevo_valor = input('Ingrese nuevo valor:')
        elemento.actualizar_valor(nuevo_valor)

def buscar_menor(lista):
    valor = input('Ingrese valor: ')
    for elemento in lista:
        if(elemento.get_valor_cuota() < valor):
            elemento.mostrar_info()
        
#def monto_licitar(lista):

def mod_cuotas(lista):
    pass

def menu(lista):
    print('1 - Actualizar valor del vehiculo')
    print('2 - Consultar vehiculos con valor de cuota menor que:')
    print('3 - Mostrar monto a pagar para licitar')
    print('4 - Modificar cantidad de cuotas para licitar')

    opcion = int(input('Opcion: '))
    match opcion:
        case 1:
            actualizar(lista)
        #case 2:
            #buscar_menor(lista)
        #case 3:
            #monto_licitar(lista)
        #case 4:
            mod_cuotas(lista)
        case _:
            print('Opcion incorrecta')

if __name__ == '__main__':
    lista = []
    archivo = open('planes.csv')
    reader = csv.reader(archivo, delimiter = ';')

    for linea in reader:
        
        lista.append(PlanAhorro(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5]))
    
    menu(lista)