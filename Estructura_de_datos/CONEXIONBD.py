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
                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_cliente TEXT NOT NULL,
                    apellidos_cliente TEXT NOT NULL
                );
            """)

            # creacion de tabla salones (turnos como INTEGER 0/1)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Salones_registrados (
                    id_salon INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_salon TEXT NOT NULL,
                    cupo INTEGER NOT NULL,
                    turno_matutino INTEGER NOT NULL DEFAULT 1 CHECK(turno_matutino IN (0,1)),
                    turno_vespertino INTEGER NOT NULL DEFAULT 1 CHECK(turno_vespertino IN (0,1)),
                    turno_nocturno INTEGER NOT NULL DEFAULT 1 CHECK(turno_nocturno IN (0,1))
                );
            """)

            # creacion de tabla reservaciones (FK correctamente escritas)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservaciones (
                    id_reservacion INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    nombre_cliente TEXT NOT NULL,
                    nombre_evento TEXT NOT NULL,
                    id_salon INTEGER NOT NULL,
                    nombre_salon TEXT NOT NULL,
                    fecha_reservacion TEXT NOT NULL,
                    turno TEXT NOT NULL CHECK (turno IN ('Matutino','Vespertino','Nocturno')),
                    estado_reservacion TEXT DEFAULT 'Activa' CHECK (estado_reservacion IN ('Activa','Cancelada')),
                    FOREIGN KEY (id_cliente) REFERENCES Clientes_registrados (id_cliente) ON DELETE CASCADE,
                    FOREIGN KEY (id_salon) REFERENCES Salones_registrados (id_salon) ON DELETE CASCADE
                );
            """)
            cursor.execute("""
                CREATE UNIQUE INDEX IF NOT EXISTS ux_reserva_unica_activa
                ON reservaciones(id_salon, fecha_reservacion, turno)
                WHERE estado_reservacion = 'Activa';
            """)

            cursor.execute("CREATE INDEX IF NOT EXISTS idx_reserva_sala_fecha ON reservaciones(id_salon, fecha_reservacion, turno);")
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except Exception:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        conn.close()