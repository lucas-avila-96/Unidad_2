from ClaseRegistro import Registro

def calcular_mayor(lista):
    for dia in lista:
        for hora in dia:
            print(f'{hora.get_temperatura}')
            print(f'{hora.get_humedad}')
            print(f'{hora.get_presion}')


def menu():

    print('Elija una opcion:')
    print('1 - Mostrar para cada variable el día y hora de menor y mayor valor. ')
    print('2 - Indicar la temperatura promedio mensual por cada hora.')
    print('3 - listar los valores de las tres variables para cada hora del día dado')

    opcion = int(input('Opcion: '))

    match opcion:
        case 1:
            print('')
        case 2:
            print('')
        case 3:
            print('')
        case _:
            print('opcion incorrecta')


if __name__ == '__main__':
    lista = [[],[]]

    for i in range(lista):
        for j in range(lista[i]):
            lista[i][j].append()

    calcular_mayor(lista)

    menu()
