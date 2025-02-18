import sqlite3


class PersonasTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla 'operaciones' con los campos id, num1, num2, operacion y resultado
        conexion = sqlite3.connect("database/tienda.db")
        try:
            conexion.execute(
                """
                create table Personas (
                                    id integer primary key autoincrement,
                                    cedula text not null, 
                                    nombre text not null,
                                    apellido text not null,
                                    telefono text not null
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla persona ya existe")
        conexion.close()

    def create(self, datos):
        # Insertar un nuevo datos en la tabla 'personas'
        conexion = sqlite3.connect("database/tienda.db")
        conexion.execute(
            "insert into Personas(cedula,nombre,apellido,telefono) values (?,?,?,?)",
            (
                datos["cedula"],
                datos["nombre"],
                datos["apellido"],
                datos["telefono"],
            ),
        )
        conexion.commit()

    def all(self):
        # Obtener todos los resultados almacenados en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        res = conexion.execute("SELECT * FROM Personas")
        return res.fetchall()
        conexion.close()

    def find(self, cedula):
        # Obtener todos los resultados almacenados en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        res = conexion.execute(
            "SELECT * FROM Personas WHERE cedula ='{}'".format(cedula)
        )
        return res.fetchone()
        conexion.close()

    def update(self, dato, cedula, opcion):
        # Actualizar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        if opcion == "1":
            conexion.execute(
                "UPDATE Personas SET cedula = '{}' WHERE cedula = '{}'".format(
                    dato, cedula
                )
            )
        elif opcion == "2":
            conexion.execute(
                "UPDATE Personas SET nombre = '{}' WHERE cedula = '{}'".format(
                    dato, cedula
                )
            )
        elif opcion == "3":
            conexion.execute(
                "UPDATE Personas SET apellido = '{}' WHERE cedula = '{}'".format(
                    dato, cedula
                )
            )
        elif opcion == "4":
            conexion.execute(
                "UPDATE Personas SET telefono = '{}' WHERE cedula = '{}'".format(
                    dato, cedula
                )
            )
        conexion.commit()
        conexion.close()

    def delete(self, cedula):
        # Eliminar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        datos = self.find(cedula)
        conexion.execute("DELETE FROM Personas WHERE id ='{}'".format(datos[0]))
        conexion.execute("DELETE FROM Compras WHERE persona_id ='{}'".format(datos[0]))
        conexion.commit()
        conexion.close()
