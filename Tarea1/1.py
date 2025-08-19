x = float(input("Ingrese un número decimal x (0 < x <= 100): "))
y = float(input("Ingrese un número decimal y (2 <= y <= 10): "))

if 0 < x <= 100 and 2 <= y <= 10:
    a = x / y
    b = x * y
    c = x - y
    d = x + y
    e = x // y
    f = x ** y

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")
    print(f"e = {e}")
    print(f"f = {f}")
else:
    print("Los números ingresados no cumplen con las condiciones especificadas.")