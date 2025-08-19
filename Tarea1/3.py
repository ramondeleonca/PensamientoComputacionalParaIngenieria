a = int(input("Ingrese el primer número (entre 1 y 10): "))
if 1 <= a <= 10:
    b = int(input("Ingrese el segundo número (entre 11 y 20): "))
    if 11 <= b <= 20:
        c = int(input("Ingrese el tercer número (entre 21 y 30): "))
        if 21 <= c <= 30:
            d1 = b - a
            d2 = c - b
            d3 = c - a

            print(f"Diferencia entre el primer y segundo número: {d1}")
            print(f"Diferencia entre el segundo y tercer número: {d2}")
            print(f"Diferencia entre el primer y tercer número: {d3}")
        else:
            print("El tercer número no está en el rango [21,30].")
    else:
        print("El segundo número no está en el rango [11,20].")
else:
    print("El primer número no está en el rango [1,10].")
