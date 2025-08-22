n1: int = None
n2: int = None
n3: int = None

while n1 is None or not (n1 >= 10 and n1 <= 20):
    n1 = int(input("Numero 1: "))

while n2 is None or not (n2 >= 30 and n2 <= 80):
    n2 = int(input("Numero 2: "))
    
while n3 is None or not (n3 >= 100 and n3 <= 120):
    n3 = int(input("Numero 3: "))

print("Los numeros son: ", n1, ", ", n2, "y", n3)
print("Los numeros estan en los rangos correctos.")