
from claseViajeroFrecuente import ViajeroFrecuente

if __name__ == '__main__':
   v1 = ViajeroFrecuente(1, 39425676, 'Lucas', 'Avila', 500)
   v2 = ViajeroFrecuente(2, 40435175, 'Juan', 'Perez', 500)
   
   print(v1 == 500)
   print(500 == v2)

   print('---ACUMULAR MILLAS---')
   
   v1 = 500 + v1
   v1 = v1 + 500
   print(v1)

   print('---CANJEAR MILLAS---')
   v2 = 100 - v2
   v2 = v2 - 100
   print(v2)

