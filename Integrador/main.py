from ClaseManejadorCama import ManejadorCama
from ClaseManejadorMedicamento import ManejadorMedicamento


if __name__ == '__main__':
    manejadorCama = ManejadorCama(1)
    manejadorMedicamento = ManejadorMedicamento()
    manejadorCama.testCamas()
    manejadorMedicamento.testMedicamentos()
    print('---ALTA DE PACIENTE---')
    print('Ingrese nombre y apellido del paciente')
    nomApe = input('Nombre y Apellido: ')
