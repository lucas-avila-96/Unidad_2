from claseEmail import Email
import csv


def cargarDatos():
    print('Ingrese los siguientes datos:')
    nombre = input('Nombre: ')
    id = input('id: ')
    dominio = input('dominio: ')
    tipo = input('tipo: ')
    contraseña = input('Contraseña: ')
    nuevaCuenta = Email(id,dominio, tipo, contraseña)
    print(f'Estimado {nombre} te enviaremos tus mensajes a la direccion {nuevaCuenta.retornaEmail()}')
    return nuevaCuenta


if __name__ == '__main__':
    cuenta1 = cargarDatos()
    cuenta1.updateContraseña()

    cuenta2 = Email()
    print('Ingrese una direccion de email')
    dir = input('Direccion: ')
    cuenta2.crearCuenta(dir)
    print('Cuenta creada')
    print(f'Id : {cuenta2.getId()}')
    print(f'Dominio : {cuenta2.getDominio()}')
    print(f'Tipo : {cuenta2.getTipo()}')

    cuentas = []
    archivo = open('correos.csv')
    reader = csv.reader(archivo, delimiter = ';')
    for line in reader:
        for correo in line:
            nueva_cuenta = Email()
            nueva_cuenta.crearCuenta(correo)
            cuentas.append(nueva_cuenta)
    print('Ingrese id para buscar')
    id = input('id: ')
    contador = 0
    
    for cuenta in cuentas:
        if id == cuenta.getId():
            contador += 1
        if contador >= 2:
            print(f'La direccion esta repetida')
            break
