
from ClaseManejadorCama import ManejadorCama
from ClaseManejadorMedicamento import ManejadorMedicamento
from ClaseCama import Cama

if __name__ == '__main__':
    manejadorCama = ManejadorCama()
    manejadorMedicamento = ManejadorMedicamento()
    manejadorCama.testCamas()
    manejadorMedicamento.testMedicamentos()

    
    print('---ALTA DE PACIENTE---')
    print('Ingrese nombre y apellido del paciente')
    nomAp = input('Nombre y Apellido: ')
    
    paciente = manejadorCama.buscarPaciente(nomAp)
    if paciente == None:
        print('No se encontro')
    else:
        id = paciente.getIdCama()
    medicamentos = manejadorMedicamento.buscarMedicamento(id)

    totalAdeudado = 0
    for m in medicamentos:
        totalAdeudado += m.getPrecio()
    
    print(f'Paciente: {paciente.getNombre()} Cama: {paciente.getIdCama()} Habitación: {paciente.getHabitacion()}')
    print(f'Diagnóstico: {paciente.getDiagnostico()} Fecha de internación: {paciente.getFechaInternacion()}')
    print(f'Fecha de Alta: {paciente.getFechaAlta()}')
    print('Medicamento/monodroga\t Presentacion\t Cantidad\t Precio')
    for medicamento in medicamentos:
        print(f'{medicamento.getMonodroga()}\t{medicamento.getPresentacion()}\t{medicamento.getCantidad()}{medicamento.getPrecio()}')
    
    print('Total adeudado: {totalAdeudado}')
