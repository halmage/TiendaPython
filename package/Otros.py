# Librerias externa
from os import system
import time


class Otros:
    def cargando(self):
        for i in range(2):
            print(".")
            time.sleep(0.5)  # Pausa de 1 segundo para visualizar el resultado

    def pausa(self):
        while True:
            respuesta = input("Ingrese la letra (s|S) para salir: ")
            if respuesta == "s" or respuesta == "S":
                Otros.cargando(self)
                system("clear")
                break

    def validacionRespuesta(self, eleccion, nombre, respuesta):
        # Validar si la respuesta es correcta
        while (
            respuesta != "y"
            and respuesta != "Y"
            and respuesta != "n"
            and respuesta != "N"
        ):
            print(
                "ERROR: la variable respuesta tiene que ser (y|Y) para seguir o (n|N) para salir"
            )
            if (
                eleccion == 1
            ):  # Validar si la eleccion es 1 para actualizar otro registro
                respuesta = input(f"Quieres actualizar [otro|otra] {nombre} (y/n): ")
            elif (
                eleccion == 2
            ):  # Validar si la eleccion es 2 para seguir actualizando el mismo registro
                respuesta = input(
                    f"Quieres seguir actualizando [el|la] {nombre} (y/n): "
                )
        return respuesta

    def respuestaSeguir(self, respuesta):
        # Validar si el usuario quiere seguir actualizando
        if respuesta == "y" or respuesta == "Y":  # (y|Y) si queiere seguir actualizando
            Otros.cargando(self)
            system("clear")
            return True
        elif (
            respuesta == "n" or respuesta == "N"
        ):  # (n|N) si no quiere seguir actualizando
            Otros.cargando(self)
            system("clear")
            return False

    def seguir(self, eleccion, nombre):
        # Validar si el usuario quiere seguir actualizando un registro
        while True:
            if (
                eleccion == 1
            ):  # Validar si la eleccion es 1 para actualizar otro registro
                respuesta = input(f"Quieres actualizar [otro|otra] {nombre} (y/n): ")
            elif (
                eleccion == 2
            ):  # Validar si la eleccion es 2 para seguir actualizando el mismo registro
                respuesta = input(
                    f"Quieres seguir actualizando [el|la] {nombre} (y/n): "
                )
            # Validar si la respuesta es correcta
            Otros.validacionRespuesta(self, eleccion, nombre, respuesta)
            # Validar si el usuario quiere seguir actualizando
            condicion = Otros.respuestaSeguir(self, respuesta)
            return condicion

    def continuar(self):
        # Validar si el usuario quiere continuar
        print("Presione la tecla enter para continuar...")
        input()
        Otros.cargando(self)
        system("clear")

    def seguirEliminando(self):
        # Validar si el usuario quiere seguir eliminando
        respuesta = input("Quieres seguir eliminando (y/n): ")
        while (
            respuesta != "y"
            and respuesta != "Y"
            and respuesta != "n"
            and respuesta != "N"
        ):
            print("ERROR: la variable respuesta tiene que ser (y|Y) o (n|N)")
            respuesta = input("Quieres seguir eliminando (y/n): ")

        if respuesta == "y" or respuesta == "Y":
            Otros.cargando(self)
            system("clear")
            return True
        else:
            Otros.cargando(self)
            system("clear")
            return False
