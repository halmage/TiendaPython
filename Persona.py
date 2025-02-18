# Librerias del sistema
from package.Otros import Otros
from database.PersonasTable import PersonasTable

# Librerias externa
from os import system
import time


class Persona:

    def create(self):
        # Ingreso de datos del usuario
        anuncio = """
        ********************************
        |INGRESO DE DATOS DE LA PERSONA|
        ********************************
        """
        print(anuncio)
        # Ingreso de cedula
        cedula = input("Cedula:")
        while cedula.isdigit() == False:
            print("ERROR: la variable cedula tiene que ser numerico")
            cedula = input("Cedula:")
        # Ingreso de nomber
        nombre = input("Nombre:")
        while nombre.isalpha() == False:
            print("ERROR: la variable nombre tiene que ser letras")
            nombre = input("Nombre:")
        # Ingreso de apellido
        apellido = input("Apellido:")
        while apellido.isalpha() == False:
            print("ERROR: la variable apellido tiene que ser letras")
            apellido = input("Apellido:")
        # Ingreso de telefono
        telefono = input("Telefono:")
        while telefono.isdigit() == False:
            print("ERROR: la variable telefono tiene que ser numerico")
            telefono = input("Telefono:")

        return {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
        }

    def find(self):
        # Mostrar los datos de la persona
        anuncio = """
        *********************
        |DATOS DE LA PERSONA|
        *********************
        """
        print(anuncio)
        # Ingreso de cedula
        cedula = input("Cedula:")
        while cedula.isdigit() == False:
            print("ERROR: la variable cedula tiene que ser numerico")
            cedula = input("Cedula:")
        print("****************")
        # Consulta en la tabla persona
        persona = PersonasTable()
        datos = persona.find(cedula)
        if datos == None:  # No hay registros en la base de datos
            Otros.cargando(self)  # Cargando
            print("No hay resultados registrados.")
            Otros.pausa(self)  # Pausa para dar continuacion al sistema
        else:  # Muestra todos los registros
            print(
                f"cedula:{datos[1]}\nnombre:{datos[2]}\napellido:{datos[3]}\ntelefono:{datos[4]}"
            )
            Otros.pausa(self)  # Pausa para dar continuacion al sistema

    def all(self):
        # Mostrar todos los resultados guardados en la base de datos
        personas = PersonasTable()
        datos = personas.all()
        if len(datos) == 0:  # No hay registros en la base de datos
            Otros.cargando(self)
            print("No hay resultados registrados.")
        else:  # Muestra todos los registros
            anuncio = """
            *********************
            |PERSONAS INGRESADAS|
            *********************
            """
            print(anuncio)
            for row in datos:
                print("\n************************")
                print(
                    f"cedula:{row[1]}\nnombre:{row[2]}\napellido:{row[3]}\ntelefono:{row[4]}"
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
        print("1. Actualizar cedula")
        print("2. Actualizar nombre")
        print("3. Actualizar apellido")
        print("4. Actualizar telefono")
        print("5. Salir")
        # Ingreso de opcion
        self.opcionUpdate = input("Elija una opcion: ")
        while self.opcionUpdate.isdigit() == False:
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcionUpdate = input("Ingrese una opcion: ")

    def datoUpdate(self, tipo_caracter):
        # Actualizar un registro de la base de datos
        campos = {
            "1": "cedula",
            "2": "nombre",
            "3": "apellido",
            "4": "telefono",
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
        ********************************
        |ACTUALIZAR DATOS DE LA PERSONA|
        ********************************
        """
        eleccion_1 = True
        while eleccion_1:
            print(anuncio)
            persona = PersonasTable()
            # Ingreso de codigo
            cedula = input("Ingrese cedula: ")
            while cedula.isdigit() == False:
                print("ERROR: la variable cedula tiene que ser numerico")
                cedula = input("Ingrese cedula: ")
            datos = persona.find(cedula)
            if datos == None:  # condicion si no se encuentra el persona
                Otros.cargando(self)  # Cargando
                print("No hay resultados registrados.")
                eleccion_1 = Otros.seguir(
                    self, 1, "persona"
                )  # segurir modificando personas
                continue
            else:  # condicion si se encuentra la persona dar la opcion de modificarlo
                eleccion_2 = True
                while eleccion_2:  # Modificando datos de la persona
                    self.menuUpdate()
                    if self.opcionUpdate < "0" or self.opcionUpdate > "5":
                        Otros.cargando(self)
                        print("ERROR: la variable opcion tiene que ser entre 1 y 5")
                        time.sleep(2)
                        system("clear")
                        continue
                    if self.opcionUpdate == "5":
                        # Salir
                        Otros.cargando(self)
                        print("Actualización cancelada")
                        time.sleep(2)
                        system("clear")
                        break
                    if self.opcionUpdate == "1":
                        # Actualizar cedula
                        dato = self.datoUpdate("numerico")
                        persona.update(dato, cedula, self.opcionUpdate)
                    elif self.opcionUpdate == "2":
                        # Actualizar nombre
                        dato = self.datoUpdate("caracter")
                        persona.update(dato, cedula, self.opcionUpdate)
                    elif self.opcionUpdate == "3":
                        # Actualizar apellido
                        dato = self.datoUpdate("caracter")
                        persona.update(dato, cedula, self.opcionUpdate)
                    elif self.opcionUpdate == "4":
                        # Actualizar telefono
                        dato = self.datoUpdate("numerico")
                        persona.update(dato, cedula, self.opcionUpdate)
                    Otros.cargando(self)
                    print("Registro actualizado correctamente")
                    eleccion_2 = Otros.seguir(
                        self, 2, "persona"
                    )  # segurir modificando el mismo personas
            eleccion_1 = Otros.seguir(
                self, 1, "persona"
            )  # segurir modificando personas

    def delete(self):
        # Eliminar un registro de la base de datos
        anuncio = """
        *********************
        |ELIMINAR PERSONA|
        *********************
        """
        print(anuncio)
        persona = PersonasTable()
        # Ingreso de cedula
        cedula = input("Cedula:")
        while cedula.isdigit() == False:
            print("ERROR: la variable cedula tiene que ser numerico")
            cedula = input("Cedula:")
        datos = persona.find(cedula)
        if datos == None:  # No hay registros en la base de datos
            Otros.cargando(self)  # Cargando
            print("No hay resultados registrados.")
            Otros.pausa(self)  # Pausa para dar continuacion al sistema
        else:  # Muestra todos los registros
            print("El registro:")
            print(
                f"cedula:{datos[1]}\nnombre:{datos[2]}\napellido:{datos[3]}\ntelefono:{datos[4]}"
            )
            persona.delete(cedula)
            Otros.cargando(self)
            print("Registro eliminado correctamente")
            time.sleep(2)
            system("clear")

    def menu(self):
        anuncio = """
        **********************
        |MENU SECCION PERSONA|
        **********************
        """
        print(anuncio)
        print("1. Ingreso de datos del usuario")
        print("2. Buscar persona")
        print("3. Visualizar datos de las personas")
        print("4. Actualizar datos de los articulos")
        print("5. Eliminar persona")
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
                print("Saliendo de la seccion persona")
                time.sleep(1)
                system("clear")
                break
            elif self.opcion == "1":
                system("clear")
                datos = self.create()
                persona_table = PersonasTable()
                persona_table.create(datos)
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
