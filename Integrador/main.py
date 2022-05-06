
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

    if paciente != None:
        id = paciente.getIdCama()
        ListaMedicamentos = manejadorMedicamento.buscarMedicamento(id)
        totalAdeudado = 0
        for medicamento in ListaMedicamentos:
            totalAdeudado += int(medicamento.getPrecio())
        
        print(f'Paciente: {paciente.getNombre()} Cama: {paciente.getIdCama()} Habitación: {paciente.getHabitacion()}')
        print(f'Diagnóstico: {paciente.getDiagnostico()} Fecha de internación: {paciente.getFechaInternacion()}')
        print(f'Fecha de Alta: {paciente.getFechaAlta()}')
        print('Medicamento/monodroga\t Presentacion\t Cantidad\t Precio')
        
        for medicamento in ListaMedicamentos:
            print(f'{medicamento.getMonodroga()}\t{medicamento.getPresentacion()}\t{medicamento.getCantidad()}{medicamento.getPrecio()}')
        
        print(f'Total adeudado: {totalAdeudado}')
    else:
        print('No se encontro')

    print('---BUSQUEDA DE PACIENTES---')
    print('ingrese nombre de diagnostico')
    nombreDiagnostico = input('Nombre: ')

    listaPacientes = manejadorCama.buscarPacienteDiagnostico(nombreDiagnostico)

    print(listaPacientes)

    if len(listaPacientes) >= 1:
        for objPaciente in listaPacientes:
            print(objPaciente)
    else:
        print(f'No se encontro ningun paciente con diagnostico {nombreDiagnostico}')
