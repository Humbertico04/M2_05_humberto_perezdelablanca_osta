def contador_caracter_especifica(letra):
    contador=0
    print('Escriba un caracter, se contarán todas las veces que uses "', letra, '"', "\n"'Utilize "." para terminar el recuento y mostrar el contador total')
    while True:
        caracter = str(input("Dime una letra: "))
        if caracter == letra:
            contador += 1
        elif caracter == ".":
            break
    return print('Has usado "', letra, '" un total de', contador, "veces.")
     
contador_caracter_especifica("a")