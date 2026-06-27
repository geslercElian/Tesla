print("    ALEXANDER NEWTOWN       ")
print(" Bienvenido a la calculadora de la familia Hellsing  ")
print("=============================================")
print("Eliga la operacion que desea realizar (Elegir el número de la operacion): ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
op = str(input("Ingrese la operacion que desea realizar: "))
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))

def swich():
    if op == "1":
        return n1 + n2
    if op == "2":
        return n1 - n2
    if op == "3":
        return n1 * n2
    



