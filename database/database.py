import sqlite3

# Crear o abrir la base de datos
conexion = sqlite3.connect("clientes.db")

# Crear un cursor para ejecutar instrucciones SQL
cursor = conexion.cursor()

# Crear la tabla clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT NOT NULL
)
""")

# Guardar los cambios
conexion.commit()

# Cerrar la conexión
conexion.close()

print("Base de datos creada correctamente.")