import sqlite3
from sqlite3 import Error
import sys
def crear_base_de_datos_y_tablas():
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()

            # activar llaves foraneas
            cursor.execute("PRAGMA foreign_keys = ON;")

            # creacion de tabla clientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Clientes_registrados (
                    id_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_cliente TEXT NOT NULL,
                    apellidos_cliente TEXT NOT NULL
                )
            """)

            # creacion de tabla salones (turnos como INTEGER 0/1)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Salones_registrados (
                    id_Salon INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_salon TEXT NOT NULL,
                    cupo INTEGER NOT NULL,
                    turno_matutino INTEGER NOT NULL DEFAULT 1,
                    turno_vespertino INTEGER NOT NULL DEFAULT 1,
                    turno_nocturno INTEGER NOT NULL DEFAULT 1
                )
            """)

            # creacion de tabla reservaciones (FK correctamente escritas)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservaciones (
                    id_reservacion INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    nombre_cliente TEXT NOT NULL,
                    nombre_evento TEXT NOT NULL,
                    id_sala INTEGER NOT NULL,
                    nombre_salon TEXT NOT NULL,
                    fecha_reservacion TEXT NOT NULL,
                    turno TEXT NOT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES Clientes_registrados (id_Cliente) ON DELETE CASCADE,
                    FOREIGN KEY (id_sala) REFERENCES Salones_registrados (id_Salon) ON DELETE CASCADE,
                    UNIQUE (id_sala, fecha_reservacion, turno)
                )
            """)
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except Exception:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        conn.close()