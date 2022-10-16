Madrid = ["Courtois", "Carvajal", "Militao", "Alaba", "Mendy", "Modric", "Kroos", "Tchouameni", "Valverde", "Vini", "Benzema"]

def caracteres_elementos_lista(lista):
    A=0
    Nombre = [lista[0]]
    LongitudMáx = len(lista[0])
    
    while True:
        print(lista[A],': ', len(lista[A]), sep="")
        A+=1
        if A == len(lista):
            break

        if LongitudMáx == len(lista[A]):
            Nombre.append(lista[A])
        elif LongitudMáx < len(lista[A]):
            Nombre = [lista[A]]
            LongitudMáx = len(lista[A])

    print("La palabra más larga es", str(Nombre), "con", LongitudMáx, "caracteres")
    return

caracteres_elementos_lista(Madrid)
