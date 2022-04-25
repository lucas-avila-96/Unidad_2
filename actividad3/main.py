import csv
from ClaseRegistro import Registro




def temp_prom_hora(lista):
    suma = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            suma += int(lista[i][j].get_temperatura())
        prom = suma/dias
        print(f'Hora: {i} Pomedio: {prom}')

def listar_variables(lista):
    print('Ingrese dia para listar')
    dia = int(input('Dia: '))
    for i in range(len(lista)):
        print(lista[i][dia - 1])

def menu(lista):

    print('Elija una opcion:')
    print('1 - Mostrar para cada variable el día y hora de menor y mayor valor. ')
    print('2 - Indicar la temperatura promedio mensual por cada hora.')
    print('3 - listar los valores de las tres variables para cada hora del día dado')

    opcion = int(input('Opcion: '))

    match opcion:
        case 1:
            pass
        case 2:
            temp_prom_hora(lista)
        case 3:
            listar_variables(lista)
        case _:
            print('opcion incorrecta')


if __name__ == '__main__':
    dias = 30
    horas = 24
    lista = []
    for i in range(horas):
        lista.append([0] * dias)
    print(lista)

    archivo = open('enero.csv')
    reader = csv.reader(archivo, delimiter = ';')
    for linea in reader:
        dia = int(linea[0])
        hora = int(linea[1])
        temp = linea[2]
        humedad = linea[3]
        presion = linea[4]
        lista[hora][dia - 1] = Registro(temp, humedad, presion)

    menu(lista)
    archivo.close()
    
