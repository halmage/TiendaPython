# Librerias del sistema
from package.Otros import Otros
from database.ArticulosTable import ArticulosTable

# Librerias externa
from os import system
import time


class Articulo:

    def create(self):
        # Ingreso de datos del usuario
        anuncio = """
        *********************************
        |INGRESO DE DATOS DE LA ARTICULO|
        *********************************
        """
        print(anuncio)
        # Ingreso de codigo
        codigo = str(input("Codigo:"))
        while codigo.isdigit() == False:
            print("ERROR: la variable codigo tiene que ser numerico")
            codigo = input("codigo:")
        # Ingreso de nombre
        nombre = str(input("Nombre:"))
        while nombre.isalpha() == False:
            print("ERROR: la variable nombre tiene que ser letras")
            nombre = input("Nombre:")
        # Ingreso de categoria
        categoria = str(input("Categoria:"))
        while categoria.isalpha() == False:
            print("ERROR: la variable categoria tiene que ser letras")
            categoria = input("Categoria:")
        # Ingreso de precio
        precio = str(input("Precio:"))
        while precio.isdigit() == False:
            print("ERROR: la variable precio tiene que ser numerico")
            precio = input("Precio:")
        # Ingreso de cantidad
        cantidad = str(input("Cantidad:"))
        while cantidad.isdigit() == False:
            print("ERROR: la variable cantidad tiene que ser numerico")
            cantidad = input("Cantidad:")
        return {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad,
        }

    def find(self):
        # Mostrar los datos del articulo
        anuncio = """
        ********************
        |DATOS DEL ARTICULO|
        ********************
        """
        print(anuncio)
        articulo = ArticulosTable()
        # Ingreso de codigo
        codigo = input("Ingrese codigo:")
        while codigo.isdigit() == False:
            print("ERROR: la variable codigo tiene que ser numerico")
            codigo = input("codigo:")
        print("****************")
        datos = articulo.find(codigo)
        if datos == None:  # No hay registros en la base de datos
            Otros.cargando(self)  # Cargando
            print("No hay resultados registrados.")
            Otros.pausa(self)  # Pausa para dar continuacion al sistema
        else:  # Muestra todos los registros
            print(
                f"codigo:{datos[1]}\nnombre:{datos[2]}\ncategoria:{datos[3]}\nprecio:{datos[4]}\ncantidad:{datos[4]}"
            )
            Otros.pausa(self)  # Pausa para dar continuacion al sistema

    def all(self):
        # Mostrar todos los resultados guardados en la base de datos
        articulos = ArticulosTable()
        datos = articulos.all()
        if len(datos) == 0:  # No hay registros en la base de datos
            Otros.cargando(self)
            print("No hay resultados registrados.")
        else:  # Muestra todos los registros
            anuncio = """
            **********************
            |ARTICULOS INGRESADOS|
            **********************
            """
            print(anuncio)
            for row in datos:
                print("\n************************")
                print(
                    f"codigo:{row[1]}\nnombre:{row[2]}\nprecio:{row[3]}\ncategoria:{row[4]}\ncantidad:{row[5]}"
                )
            Otros.pausa(self)  # Pausa para dar continuacion al sistema

    def menuUpdate(self):
        # Menu para actualizar un registro
        anuncio = """
        ***************************
        |MENU ACTUALIZAR ARTICULO|
        ***************************
        """
        print(anuncio)
        print("1. Actualizar codigo")
        print("2. Actualizar nombre")
        print("3. Actualizar categoria")
        print("4. Actualizar precio")
        print("5. Actualizar cantidad")
        print("6. Salir")
        # Ingreso de opcion
        self.opcionUpdate = input("Elija una opcion: ")
        while self.opcionUpdate.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcionUpdate = input("Ingrese una opcion: ")

    def datoUpdate(self, tipo_caracter):
        campos = {
            "1": "codigo",
            "2": "nombre",
            "3": "categoria",
            "4": "precio",
            "5": "cantidad",
        }
        # Actualizar codigo
        if tipo_caracter == "numerico":
            dato = input(f"Ingrese {campos[self.opcionUpdate]}:")
            while dato.isdigit() == False:
                print(
                    f"ERROR: la variable {campos[self.opcionUpdate]} tiene que ser numerico"
                )
                dato = input(f"Ingrese {campos[self.opcionUpdate]}:")
            return dato
        elif tipo_caracter == "caracter":
            dato = input(f"Ingrese {campos[self.opcionUpdate]}:")
            while dato.isalpha() == False:
                print(
                    f"ERROR: la variable {campos[self.opcionUpdate]} tiene que ser caracter"
                )
                dato = input(f"Ingrese {campos[self.opcionUpdate]}:")
            return dato

    def update(self):
        # Actualizar un registro de la base de datos
        anuncio = """
        ********************
        |ACTUALIZAR ARTICULO|
        ********************
        """
        eleccion_1 = True
        while eleccion_1:
            print(anuncio)
            articulo = ArticulosTable()
            # Ingreso de codigo
            codigo = input("Ingrese codigo: ")
            while codigo.isdigit() == False:
                print("ERROR: la variable codigo tiene que ser numerico")
                codigo = input("codigo: ")
            datos = articulo.find(codigo)
            if datos == None:  # condicion si no se encuentra el articulo
                Otros.cargando(self)  # Cargando
                print("No hay resultados registrados.")
                eleccion_1 = Otros.seguir(
                    self, 1, "articulo"
                )  # segurir modificando articulos
                continue
            else:  # condicion si no se encuentra el articulo dar la opcion de modificarlo
                eleccion_2 = True
                while eleccion_2:  # Modificando un articulo
                    self.menuUpdate()
                    if self.opcionUpdate < "0" or self.opcionUpdate > "6":
                        Otros.cargando(self)
                        print("ERROR: la variable opcion tiene que ser entre 1 y 6")
                        time.sleep(2)
                        system("clear")
                        continue
                    if self.opcionUpdate == "6":
                        # Salir
                        Otros.cargando(self)
                        print("Actualización cancelada")
                        time.sleep(2)
                        system("clear")
                        break
                    if self.opcionUpdate == "1":
                        # Actualizar codigo
                        dato = self.datoUpdate("numerico")
                        articulo.update(dato, codigo, self.opcionUpdate)
                    elif self.opcionUpdate == "2":
                        # Actualizar nombre
                        dato = self.datoUpdate("caracter")
                        articulo.update(dato, codigo, self.opcionUpdate)
                    elif self.opcionUpdate == "3":
                        # Actualizar categoria
                        dato = self.datoUpdate("caracter")
                        articulo.update(dato, codigo, self.opcionUpdate)
                    elif self.opcionUpdate == "4":
                        # Actualizar precio
                        dato = self.datoUpdate("numerico")
                        articulo.update(dato, codigo, self.opcionUpdate)
                    elif self.opcionUpdate == "5":
                        # Actualizar cantidad
                        dato = self.datoUpdate("numerico")
                        articulo.update(dato, codigo, self.opcionUpdate)
                    Otros.cargando(self)
                    print("Registro actualizado correctamente")
                    eleccion_2 = Otros.seguir(
                        self, 2, "articulo"
                    )  # segurir modificando el mismo articulos
            eleccion_1 = Otros.seguir(
                self, 1, "articulo"
            )  # segurir modificando articulos

    def delete(self):
        # Eliminar un registro de la base de datos
        condicion = True
        while condicion:
            anuncio = """
            *******************
            |ELIMINAR ARTICULO|
            *******************
            """
            print(anuncio)
            articulo = ArticulosTable()
            # Ingreso de codigo
            codigo = input("Ingrese codigo:")
            while codigo.isdigit() == False:
                print("ERROR: la variable codigo tiene que ser numerico")
                codigo = input("codigo:")
            datos = articulo.find(codigo)
            if datos == None:  # No hay registros en la base de datos
                Otros.cargando(self)  # Cargando
                print("No hay resultados registrados.")
            else:  # Muestra todos los registros
                print("El registro:")
                print(
                    f"codigo:{datos[1]}\nnombre:{datos[2]}\nprecio:{datos[3]}\ncategoria:{datos[4]}\ncantidad:{datos[5]}"
                )
                articulo.delete(codigo)
                Otros.cargando(self)
                print("Registro eliminado correctamente")
                time.sleep(2)
                system("clear")
            condicion = Otros.seguirEliminando(self)

    def menu(self):
        anuncio = """
        ***********************
        |MENU SECCION ARTICULO|
        ***********************
        """
        print(anuncio)
        print("1. Ingreso de datos del articulo")
        print("2. Buscar articulo")
        print("3. Visualizar datos de los articulos")
        print("4. Actualizar datos de los articulos")
        print("5. Eliminar articulo")
        print("6. Salir")
        # Ingreso de opcion
        self.opcion = input("Elija una opcion: ")
        while self.opcion.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def operaciones(self):
        while True:
            self.menu()
            if self.opcion == "6":
                # salida del sistema
                Otros.cargando(self)
                print("Saliendo de la seccion articulo")
                time.sleep(1)
                system("clear")
                break
            elif self.opcion == "1":
                system("clear")
                datos = self.create()
                articulo = ArticulosTable()
                articulo.create(datos)
                Otros.cargando(self)
                print("Datos ingresados correctamente")
                time.sleep(1)
                system("clear")
            elif self.opcion == "2":
                system("clear")
                self.find()
            elif self.opcion == "3":
                system("clear")
                self.all()
            elif self.opcion == "4":
                system("clear")
                self.update()
            elif self.opcion == "5":
                system("clear")
                self.delete()
