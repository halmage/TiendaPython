# Librerias del sistema
import sqlite3


class ComprasTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla 'operaciones' con los campos id, num1, num2, operacion y resultado
        conexion = sqlite3.connect("database/tienda.db")
        try:
            conexion.execute(
                """
                create table compras (
                                    id integer primary key autoincrement,
                                    persona_id integer not null, 
                                    articulo_id integer not null,
                                    cantidad integer not null,
                                    total integer not null,                                    
                                    FOREIGN KEY (persona_id) 
                                    REFERENCES Personas (id) 
                                        ON DELETE CASCADE 
                                        ON UPDATE CASCADE
                                    FOREIGN KEY (articulo_id) 
                                    REFERENCES Articulos (id) 
                                        ON DELETE CASCADE 
                                        ON UPDATE CASCADE
                                )"""
            )
        except sqlite3.OperationalError:
            print("La tabla persona_articulos ya existe")
        conexion.close()

    def create(self, datos):
        # Insertar un nuevo resultado en la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        conexion.execute(
            "insert into Compras(persona_id,articulo_id,cantidad,total) values (?,?,?,?)",
            (
                datos["persona_id"],
                datos["articulo_id"],
                datos["cantidad_articulo"],
                datos["total_compra"],
            ),
        )
        conexion.execute(
            "UPDATE Articulos SET cantidad = {} WHERE id = {}".format(
                datos["cantidad_restante"],
                datos["articulo_id"],
            )
        )
        conexion.commit()

    def findAll(self):
        # Buscar todos los resultados de la tabla 'operaciones'
        conexion = sqlite3.connect("database/tienda.db")
        cursor = conexion.execute(
            """
            SELECT Personas.cedula,
                      Personas.nombre,
                      Personas.apellido,
                      Personas.telefono,            
                      Articulos.codigo,
                      Articulos.nombre,
                      Articulos.categoria,
                      Articulos.precio,
                      Compras.cantidad,
                      Compras.total                      
                      FROM Compras INNER JOIN Personas ON Compras.persona_id = Personas.id 
                      INNER JOIN Articulos ON Compras.articulo_id = Articulos.id
                      """
        )
        return cursor.fetchall()
