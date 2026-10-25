from services.cliente_service import crear_cliente, obtener_clientes


def registrar():
    print("\n===== REGISTRO DE CLIENTE =====")

    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    mensaje = crear_cliente(nombre, telefono, correo)

    print(mensaje)


def listar():
    print("\n===== LISTA DE CLIENTES =====")

    clientes = obtener_clientes()

    for cliente in clientes:
        print(f"ID: {cliente[0]}")
        print(f"Nombre: {cliente[1]}")
        print(f"Teléfono: {cliente[2]}")
        print(f"Correo: {cliente[3]}")
        print("-----------------------------")