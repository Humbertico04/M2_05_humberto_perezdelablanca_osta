A = float(input("Dime un número: "))
B = float(input("Dime otro número: "))
C = float(input("Dime un número más: "))

lista=[A, B, C]

def orden_numeros_lista(lista):
    if sorted(lista)==lista and list(reversed(sorted(lista)))==lista:
     entrada=print("Son todos los mismos números")
    elif list(reversed(sorted(lista)))==lista:
        entrada=print("Los números están en orden descendente")
    elif sorted(lista)==lista:
        entrada=print("Los números están en orden ascendente")
    else:
        entrada=print("Los números no están en orden")
    return entrada

orden_numeros_lista(lista)