import sqlite3


class ArticulosTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla 'operaciones' con los campos id, num1, num2, operacion y resultado
        conexion = sqlite3.connect("database/tienda.db")
        try:
            conexion.execute(
                """
                create table Articulos (
                                    id integer primary key autoincrement,
                                    codigo text not null, 
                                    nombre text not null,
                                    categoria text not null,                                    
                                    precio integer not null,
                                    cantidad integer not null
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla articulos ya existe")
        conexion.close()

    def create(self, resultado):
        # Insertar un nuevo resultado en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        conexion.execute(
            "insert into Articulos(codigo,nombre,categoria,precio,cantidad) values (?,?,?,?,?)",
            (
                resultado["codigo"],
                resultado["nombre"],
                resultado["categoria"],
                resultado["precio"],
                resultado["cantidad"],
            ),
        )
        conexion.commit()

    def all(self):
        # Obtener todos los resultados almacenados en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        res = conexion.execute("SELECT * FROM Articulos")
        return res.fetchall()
        conexion.close()

    def find(self, codigo):
        # Obtener todos registro de un articulo
        conexion = sqlite3.connect("database/tienda.db")
        res = conexion.execute(
            "SELECT * FROM Articulos WHERE codigo ='{}'".format(codigo)
        )
        return res.fetchone()
        conexion.close()

    def update(self, dato, codigo, opcion):
        # Actualizar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        if opcion == "1":
            conexion.execute(
                "UPDATE Articulos SET codigo = '{}' WHERE codigo = '{}'".format(
                    dato, codigo
                )
            )
        elif opcion == "2":
            conexion.execute(
                "UPDATE Articulos SET nombre = '{}' WHERE codigo = '{}'".format(
                    dato, codigo
                )
            )
        elif opcion == "3":
            conexion.execute(
                "UPDATE Articulos SET categoria = '{}' WHERE codigo = '{}'".format(
                    dato, codigo
                )
            )
        elif opcion == "4":
            conexion.execute(
                "UPDATE Articulos SET precio = '{}' WHERE codigo = '{}'".format(
                    dato, codigo
                )
            )
        elif opcion == "5":
            conexion.execute(
                "UPDATE Articulos SET cantidad = '{}' WHERE codigo = '{}'".format(
                    dato, codigo
                )
            )
        conexion.commit()
        conexion.close()

    def delete(self, codigo):
        # Eliminar un registro de la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        datos = self.find(codigo)
        conexion.execute("DELETE FROM Articulos WHERE id ='{}'".format(datos[0]))
        conexion.execute("DELETE FROM Compras WHERE articulo_id ='{}'".format(datos[0]))
        conexion.commit()
        conexion.close()
