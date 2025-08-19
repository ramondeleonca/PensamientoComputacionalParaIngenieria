n1: int = 0
n2: int = 0

while not (n1 >= 10 and n1 <= 20):
    n1 = int(input("Numero 1: "))

while not (n2 >= -15 and n2 <= -5):
    n2 = int(input("Numero 2: "))

print("Los numeros son: ", n1, "y", n2)
print("Los numeros estan en los rangos correctos.")