from ClaseConjunto import Conjunto

def test():
    objetoPruba = Conjunto([1, 2, 3, 4])
    print(objetoPruba)

if __name__ == '__main__':
    test()
    A = Conjunto([1, 2, 3, 4])
    B = Conjunto([3, 6, 9])
    C = Conjunto([1, 2, 3])
    D = Conjunto([1, 2, 3])

    C1 = A + B 
    print(f'{A} + {B} = {C1}')

    C2 = A - B
    print(f'{A} - {B} = {C2}')

    esIgual = C == D
    print(esIgual)

