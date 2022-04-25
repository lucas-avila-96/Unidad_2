import csv
from ClaseCama import Cama
from ClaseMedicamento import Medicamento


if __name__ == '__main__':
    archivo = open('camas.csv')
    reader = csv.reader(archivo, delimiter = ';')
    next(reader)
    camas = []

    for fila in reader:
        camas.append(Cama(fila[0], fila[1], bool(fila[2]), fila[3], fila[4], (fila[5])))
    
    print(camas[0])