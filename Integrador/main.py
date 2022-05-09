
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
        fechaAlta = input('Fecha de alta: ')
        paciente.setFechaAlta(fechaAlta)
        paciente.setEstado()
        id = paciente.getIdCama()
        ListaMedicamentos = manejadorMedicamento.buscarMedicamento(id)
        totalAdeudado = 0
        for medicamento in ListaMedicamentos:
            totalAdeudado += int(medicamento.getPrecio())
        
        print('{}{:<25}{}{:<10}{}{:<10}'.format('Paciente: ', paciente.getNombre(),'Cama:', paciente.getIdCama(),'Habitación: ', paciente.getHabitacion()))
        print('{}{:<25}{}{:<10}'.format('Diagnóstico:', paciente.getDiagnostico(), 'Fecha de internación:',paciente.getFechaInternacion()))
        print('{}{:<25}'.format('Fecha de Alta:', paciente.getFechaAlta()))
        print('{:<30}{:<20}{:<20}{:<20}'.format('Medicamento/monodroga', 'Presentacion', 'Cantidad', 'Precio'))
        
        for medicamento in ListaMedicamentos:
            print('{:<9}{}{:<20}{:<20}{:<20}{:<20}'.format(medicamento.getNombre(),'/', medicamento.getMonodroga(), medicamento.getPresentacion(), medicamento.getCantidad(), medicamento.getPrecio()))
        print('{:<30}{:<20}{:<20}{:<20}'.format('Total adeudado:','','', totalAdeudado))
    else:
        print('No se encontro')

    print('---BUSQUEDA DE PACIENTES---')
    print('ingrese nombre de diagnostico')
    nombreDiagnostico = input('Nombre: ')

    listaPacientes = manejadorCama.buscarPacienteDiagnostico(nombreDiagnostico)

    if len(listaPacientes) >= 1:
        for objPaciente in listaPacientes:
            print(objPaciente)
    else:
        print(f'No se encontro ningun paciente con diagnostico {nombreDiagnostico}')
