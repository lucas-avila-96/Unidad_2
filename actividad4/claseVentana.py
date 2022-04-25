class Ventana:
    __titulo = ''
    __x1 = 0
    __y1 = 0
    __x2 = 0
    __y2 = 0

    def __init__(self, titulo, x1 = 0, y1 = 0, x2 = 500, y2 = 500):
        self.__titulo = titulo
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    def getTitulo(self):
        return self.__titulo

    def mostrar(self):
        print(f'Vertice superior: ({self.__x1}, {self.__y1})')
        print(f'Vertice inferior: ({self.__x2}, {self.__y2})')
    
    def alto(self):
        return self.__y2 - self.__y1
    
    def ancho(self):
        return self.__x2 - self.__x1

    def moverDerecha(self, n = 1):
        self.__x1 += n
        self.__x2 += n
    
    def moverIzquierda(self, n = 1):
        self.__x1 -= n
        self.__x2 -= n
    
    def bajar(self, n = 1):
        self.__y1 += n
        self.__y2 += n

    def subir(self, n = 1):
        self.__y1 -= n
        self.__y2 -= n
        

