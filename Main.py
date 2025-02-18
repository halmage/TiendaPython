# Librerias del sistema
from package.Otros import Otros
from database.ComprasTable import ComprasTable
from database.PersonasTable import PersonasTable
from database.ArticulosTable import ArticulosTable


# Clases
from Compra import Compra
from Persona import Persona
from Articulo import Articulo


# Librerias externa
from os import system
import time


class Main:
    def menu(self):
        anuncio = """
        ****************
        |MENU PRINCIPAL|
        ****************
        """
        print(anuncio)
        print("0. Crear base de datos")
        print("1. Modula personas")
        print("2. Modulo articulos")
        print("3. Modulo compras")
        print("4. Salir")
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def operaciones(self):
        while True:
            self.menu()
            if self.opcion == "4":
                # salida del sistema
                Otros.cargando(self)
                print("Gracias por utilizar nuestro sistema")
                time.sleep(1)
                system("clear")
                break
            elif self.opcion == "0":
                # creacion de base de datos
                # Creando tabla persona
                persona_table = PersonasTable()
                persona_table.createDatabase()
                # Creando tabla articulo
                articulo_table = ArticulosTable()
                articulo_table.createDatabase()
                # Creando tabla Compras
                compras_table = ComprasTable()
                compras_table.createDatabase()
                Otros.cargando(self)
                print("Base de datos creada correctamente")
                time.sleep(1)
                system("clear")
                continue
            elif self.opcion == "1":
                # Modulo persona
                Otros.cargando(self)
                print("Modulo persona")
                time.sleep(1)
                system("clear")
                persona = Persona()
                persona.operaciones()
            elif self.opcion == "2":
                # Modulo articulo
                Otros.cargando(self)
                print("Modulo articulo")
                time.sleep(1)
                system("clear")
                articulo = Articulo()
                articulo.operaciones()
            elif self.opcion == "3":
                # Modulo articulo
                Otros.cargando(self)
                print("Modulo compra")
                time.sleep(1)
                system("clear")
                compra = Compra()
                compra.operaciones()


main = Main()
main.operaciones()
