from dao.cliente_dao import registrar_cliente, listar_clientes


def crear_cliente(nombre, telefono, correo):
    registrar_cliente(nombre, telefono, correo)
    return "Cliente registrado correctamente."


def obtener_clientes():
    return listar_clientes()