def comparar_tres_números(A, B, C):
    if A==B==C:
        entrada=print("Son los mismos números")
    elif A<=B<=C:
        entrada=print("Los números están en orden ascendente")
    elif A>=B>=C:
        entrada=print("Los números están en orden descendente")
    else:
        entrada=print("Los números no están en orden numérico")
    return entrada

def comparar_tres_números_pedidos():
    A = float(input("Dime un número: "))
    B = float(input("Dime otro número: "))
    C = float(input("Dime un número más: "))
    return comparar_tres_números(A, B, C)

comparar_tres_números_pedidos()