import sqlite3
from sqlite3 import Error
import sys
from tabulate import tabulate   
#aqui creamos la conexion a la base de datos, le ponemos el nombre que llevara y la tabla amigos si no existe
try:
    with sqlite3.connect("sistema_de_amigos.db") as conn:
        mi_primer_cursor=conn.cursor()
        mi_primer_cursor.execute("CREATE TABLE IF NOT EXISTS amigos (id_amigo INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellidos TEXT NOT NULL);")
        print("Base de datos y tabla creada exitosamente.\n")
except Error as e:
    print(f"Ocurrio un error al crear la base de datos: {e}\n")
except:
    print(f"Ocurrio un error inesperado: {sys.exc_info()[0]}\n")


while True:
    print(f"{'*'*60}")
    print("\tBienvenido al sistema de registro de amigos.")
    print(f"{'-'*60}\n")
    print("1. Agregar un nuevo amigo")
    print("2. consultar datos de un amigo")
    print("3. Ver lista de amigos")
    print("4. Salir\n")
    opcion=input("Que opcion eliges? ")
    if opcion=="4":
        print("Saliendo del sistema...")
        break
    elif opcion=="1":
        print(f"\n{'*'*60}")
        print("\tVamos a agregar un nuevo amigo")
        print(f"{'-'*60}\n")

        nombre_amigo=input("Escribe el nombre de tu amigo: ").strip().upper()
        apellidos_amigo=input("Escribe los apellidos de tu amigo: ").strip().upper()

        if nombre_amigo=="" or apellidos_amigo=="":
            print("\nDebes de ingresar un nombre y apellidos validos!\n")
            continue
        elif all(letra.isalpha() or letra.isspace() for letra in nombre_amigo) and all(letra.isalpha() or letra.isspace() for letra in apellidos_amigo):
            try:
                with sqlite3.connect("sistema_de_amigos.db") as conn:
                    mi_cursor_amigos=conn.cursor()
                    mi_cursor_amigos.execute("INSERT INTO amigos (nombre, apellidos) VALUES (?, ?);", (nombre_amigo, apellidos_amigo))
                    print(f"\nAmigo {nombre_amigo} {apellidos_amigo} agregado exitosamente con el id: {mi_cursor_amigos.lastrowid}.\n")
            except Error as e:
                print(f"Ocurrio un error al agregar el amigo: {e}")
            except:
                print(f"Ocurrio un error inesperado: {sys.exc_info()[0]}")
            finally:
                conn.close()    
        else:
            print("\nDebes de ingresar un nombre y apellidos validos!\n")
            continue 
    elif opcion=="2":
        print(f"\n{'*'*60}")
        print("\tVamos a consultar los datos de un amigo")
        print(f"{'-'*60}\n")
        
        id_amigo_consulta=input("Escribe el id del amigo que quieres consultar: ")
        try:
            with sqlite3.connect("sistema_de_amigos.db") as conn:
                mi_cursor_consulta=conn.cursor()
                mi_cursor_consulta.execute("SELECT * FROM amigos WHERE id_amigo = ?;", (int(id_amigo_consulta),))
                amigo_encontrado=mi_cursor_consulta.fetchone()
                if amigo_encontrado:
                    print(tabulate([amigo_encontrado], headers=["ID Amigo", "Nombre", "Apellidos"], tablefmt="fancy_grid"))
                else:
                    print(f"\nNo se encontro ningun amigo con el id {id_amigo_consulta}.\n")
        except Error as e:
            print(f"\nOcurrio un error al consultar el amigo: {e}")
        except:
            print(f"\nOcurrio un error inesperado: {sys.exc_info()[0]}")
        finally:
            conn.close()

    elif opcion=="3":
        print(f"\n{'*'*60}")
        print("\tLista de todos tus amigos")
        print(f"{'-'*60}\n")
        try:
            with sqlite3.connect("sistema_de_amigos.db") as conn:
                mi_cursor_lista_amigos=conn.cursor()
                mi_cursor_lista_amigos.execute("SELECT * FROM amigos;")
                amigos_encontrados=mi_cursor_lista_amigos.fetchall()

                if amigos_encontrados:
                    print(tabulate(amigos_encontrados,headers=["Id amigo","Nombre amigo","Apellidos amigo"],tablefmt="fancy_grid"))
                else:
                    print(f"{'*'*60}\n")
                    print("--Aviso: No tienes amigos registrados aun.--\n")
                    print(f"{'*'*60}\n")
        except Error as e:
            print(f"\nOcurrio un error al obetner la lista de amigos: {e}")
        except:
            print(f"\nOcurrio un error inesperado: {sys.exc_info()[0]}")
        finally:
            conn.close()
    else:
        print("\nDebes de elegir una opcion valida!\n")
        continue