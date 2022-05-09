from database.db import obtener_conexion

def insertar_trabajo(nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO trabajos(nombre, descripcion, precio) VALUES (%s, %s, %s)",
                       (nombre, descripcion, precio))
    conexion.commit()
    conexion.close()

def obtener_trabajos():
    conexion = obtener_conexion()
    trabajos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, descripcion, precio FROM trabajos")
        trabajos = cursor.fetchall()
    conexion.close()
    return trabajos

def eliminar_trabajo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM trabajos WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_trabajo_por_id(id):
    conexion = obtener_conexion()
    trabajo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, descripcion, precio FROM trabajos WHERE id = %s", (id,))
        trabajo = cursor.fetchone()
    conexion.close()
    return trabajo

def actualizar_trabajo(nombre, descripcion, precio, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE trabajos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
                       (nombre, descripcion, precio, id))
    conexion.commit()
    conexion.close()