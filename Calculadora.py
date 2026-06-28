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

def Olly():
    if op == "1":
        return n1 + n2
    if op == "2":
        return n1 - n2
    if op == "3":
        return n1 * n2
    if op == "4":
        return n1 / n2
print("El resultado de la operacion es: ", Olly())

if Olly() < 10:
    print("A ti te toca quedarte con Alexander :)")
elif Olly() > 10 and Olly() < 20:
    print("A ti te toca quedarte con Elian :(")
elif Olly() > 20 and Olly() < 30:
    print("A ti te toca quedarte con Alucard :)")
else:
    print("A ti te toca quedarte con absolutamente nada :)")