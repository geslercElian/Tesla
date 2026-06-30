from os import system
if system("clear") != 0: system("cls")
import random as pepepollo 
juego = ["Piedra", "Papel", "Tijera"]
pc = pepepollo.choice(juego)
usuario = input("Ingrese su jugada: ")
if usuario == pc:
    print("Empate, ambos eligieron: ", pc)
elif usuario == "Piedra" and pc == "Tijera":
    print("Ganaste, la computadora eligió: ", pc)
elif usuario == "Papel" and pc == "Piedra":
    print("Ganaste, la computadora eligió: ", pc)
elif usuario == "Tijera" and pc == "Papel":
    print("Ganaste, la computadora eligió: ", pc)
else:
    print("Perdiste, la computadora eligió: ", pc)