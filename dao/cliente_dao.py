import sqlite3

def registrar_cliente(nombre, telefono, correo):
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO clientes (nombre, telefono, correo)
        VALUES (?, ?, ?)
    """, (nombre, telefono, correo))

def listar_clientes():
    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, telefono, correo FROM clientes")

    clientes = cursor.fetchall()

    conexion.close()

    return clientes

    conexion.commit()
    conexion.close()