from ClaseConjunto import Conjunto

if __name__ == '__main__':
    A = Conjunto([1, 2, 3, 4])
    B = Conjunto([3, 6, 9])
    C = Conjunto([1, 2, 3])
    D = Conjunto([1, 2, 3])

    C1 = A + B 
    print(C1)

    C2 = A - B
    print(C2)

    C3 = C == D
    print(C3)

