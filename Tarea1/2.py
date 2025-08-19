a = int(input("Ingrese el primer número entero positivo (a): "))
b = int(input("Ingrese el segundo número entero positivo (b): "))

if a <= 0 or b <= 0 or b < 2 * a:
    print("Error: ambos números deben ser enteros positivos y el segundo número debe ser al menos el doble del primero.")
else:
    y = 3*a**4 + 2*b**2 + 4*(a**2)*(b**3) - 10*(b**3) - 20*a*b - 5
    print(f"El valor de y es: {y}")