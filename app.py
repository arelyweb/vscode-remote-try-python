#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random
def juego_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    opciones_dict = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

    print("Bienvenido al juego de piedra, papel o tijera")
    print("Para jugar, ingresa una de las siguientes opciones: piedra, papel o tijera")
    print("Para salir, ingresa la palabra salir")
    print("")

    while True:
        jugador = input("Ingresa tu jugada: ")
        jugador = jugador.lower()
        computadora = random.choice(opciones)

        if jugador == "salir":
            break
        elif jugador not in opciones:
            print("Ingresa una opción válida")
            print("")
        elif jugador == computadora:
            print("Empate!")
            print("")
        elif opciones_dict[jugador] == computadora:
            print("Ganaste!")
            print("")
        else:
            print("Perdiste!")
            print("")
    print("Gracias por jugar!")

juego_piedra_papel_tijera()