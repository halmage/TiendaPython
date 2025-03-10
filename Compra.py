# Librerias del sistema
from package.Otros import Otros
from database.ComprasTable import ComprasTable
from database.PersonasTable import PersonasTable
from database.ArticulosTable import ArticulosTable

# Librerias externa
from os import system
import time


class Compra:

    def ingresandoCedulaComprador(self):
        # Ingreso de cedula del comprador
        cedula_comprador = input("Cedula del comprador:")
        while cedula_comprador.isdigit() == False:
            print("ERROR: la variable cedula del comprador tiene que ser numerico")
            cedula_comprador = input("Cedula del comprador:")
        # Consulta en la tabla personas
        persona = PersonasTable()
        datos_persona = persona.find(cedula_comprador)
        while datos_persona == None:
            print(f"La cedula {cedula_comprador} no se encuentra en el sistema")
            cedula_comprador = input("Cedula del comprador:")
            datos_persona = persona.find(cedula_comprador)
        return datos_persona

    def ingresaCodigoArticulo(self):
        # Ingreso de codigo del articulo
        codigo_articulo = input("Codigo del articulo:")
        while codigo_articulo.isdigit() == False:
            print("ERROR: la variable codigo del articulo tiene que ser numerico")
            codigo_articulo = input("Codigo del articulo:")
        # Consulta en la tabla articulos
        articulo = ArticulosTable()
        datos_articulo = articulo.find(codigo_articulo)
        while datos_articulo == None:
            print(f"El codigo {codigo_articulo} no se encuentra en el sistema")
            codigo_articulo = input("Codigo del articulo:")
            datos_articulo = articulo.find(codigo_articulo)
        return datos_articulo

    def validandoCantidadArticulos(self, datos_articulo):
        # Ingreso de cantidad de articulos que desea comprar la persona
        cantidad_articulo = str(input("Cantidad de articulos:"))
        while cantidad_articulo.isdigit() == False:
            print("ERROR: la variable cantidad tiene que ser numerico")
            cantidad_articulo = input("Cantidad:")
        # Validacion de la cantidad de articulos
        while int(cantidad_articulo) > datos_articulo[5]:
            print(
                f"ERROR: La cantidad de articulos que desea no se encuentra en nuestro stock solo tenemos {datos_articulo[5]}"
            )
            cantidad_articulo = input("Cantidad de articulos:")
        cantidad_restante = datos_articulo[5] - int(
            cantidad_articulo
        )  # Restandole articulos al stock
        return {
            "cantidad_articulo": cantidad_articulo,
            "cantidad_restante": cantidad_restante,
        }

    def totalDeLaCompra(self, cantidad_articulo, datos_articulo):
        total = int(cantidad_articulo) * int(datos_articulo[4])  # Total de la compra
        return total

    def create(self):
        # Ingreso de datos de la compra
        anuncio = """
        ************************************
        |INGRESO DE DATOS DE LA COMPRA|
        ************************************
        """
        print(anuncio)
        datos_persona = self.ingresandoCedulaComprador()
        datos_articulo = self.ingresaCodigoArticulo()
        datos_cantidad = self.validandoCantidadArticulos(datos_articulo)
        total_compra = self.totalDeLaCompra(
            datos_cantidad["cantidad_articulo"], datos_articulo
        )

        return {
            "persona_id": datos_persona[0],
            "articulo_id": datos_articulo[0],
            "cantidad_articulo": datos_cantidad["cantidad_articulo"],
            "cantidad_restante": datos_cantidad["cantidad_restante"],
            "total_compra": total_compra,
        }

    def find(self):
        anuncio = """
            ****************************************
            |BUSQUEDA DE LAS COMPRAS DE UNA PERSONA|
            ****************************************
            """
        respuesta = True
        while respuesta:
            print(anuncio)
            cedula = input("Cedula de la persona:")
            while cedula.isdigit() == False:
                print("ERROR: la variable cedula tiene que ser numerico")
                cedula = input("Cedula de la persona:")
            compra_table = ComprasTable()
            datos = compra_table.find(cedula)
            if len(datos) == 0:
                anuncio = """
                *******************************************************
                |NO HAY COMPRAS DE LA PERSONA REGISTRADA EN EL SISTEMA|
                *******************************************************
                """
                print(anuncio)
            else:
                for dato in datos:
                    print("*********************************")
                    print(f"Cedula: {dato[0]}")
                    print(f"Persona: {dato[1]} {dato[2]}")
                    print(f"Tlf: {dato[3]}")
                    print(f"Codigo del articulo: {dato[4]}")
                    print(f"Nombre del articulo: {dato[5]}")
                    print(f"Categoria del articulo: {dato[6]}")
                    print(f"Precio del articulo: {dato[7]}")
                    print(f"Cantidad de articulos: {dato[8]}")
                    print(f"Total de la compra: {dato[9]}")
                    print("*********************************")
            consulta = input("Quieres seguir buscando una compra (y/n):")
            respuesta = Otros.respuestaSeguir(self, consulta)

    def findAll(self):
        compra_table = ComprasTable()
        compras = compra_table.findAll()
        if len(compras) == 0:
            anuncio = """
            ******************************
            |NO HAY COMPRAS EN EL SISTEMA|
            ******************************
            """
            print(anuncio)  # Mensaje de error
            return
        anuncio = """
        *********************************
        |COMPRAS REALIZADAS POR PERSONAS|
        *********************************
        """
        print(anuncio)
        for dato in compras:
            print("*********************************")
            print(f"Cedula: {dato[0]}")
            print(f"Persona: {dato[1]} {dato[2]}")
            print(f"Tlf: {dato[3]}")
            print(f"Codigo del articulo: {dato[4]}")
            print(f"Nombre del articulo: {dato[5]}")
            print(f"Categoria del articulo: {dato[6]}")
            print(f"Precio del articulo: {dato[7]}")
            print(f"Cantidad de articulos: {dato[8]}")
            print(f"Total de la compra: {dato[9]}")
            print("*********************************")

    def menu(self):
        anuncio = """
        **********************
        |MENU SECCION PERSONA|
        **********************
        """
        print(anuncio)
        print("1. Comprar articulos")
        print("2. buscar compras de una persona")
        print("3. Visualizar compras de las personas")
        print("4. Salir")
        # Ingreso de opcion
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
                print("Saliendo de la seccion compra")
                time.sleep(1)
                system("clear")
                break
            if self.opcion == "1":
                system("clear")
                datos = self.create()
                compra_table = ComprasTable()
                compra_table.create(datos)
                Otros.cargando(self)
                print("Datos ingresados correctamente")
                time.sleep(2)
                system("clear")
            elif self.opcion == "2":
                system("clear")
                self.find()
            elif self.opcion == "3":
                system("clear")
                self.findAll()
                Otros.continuar(self)
