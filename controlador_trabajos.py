from database.db import obtener_conexion

def insertar_trabajo(nombre, descripcion, precio, path_imagen, id_categoria):
    conexion = obtener_conexion()
    sql_query = "INSERT INTO trabajos(nombre, descripcion, precio, imagen, id_categoria) VALUES (%s, %s, %s, %s, %s)"
    with conexion.cursor() as cursor:
        cursor.execute(sql_query,(nombre, descripcion, precio, path_imagen, id_categoria))
    conexion.commit()
    conexion.close()

def obtener_trabajos():
    conexion = obtener_conexion()
    trabajos = []
    sql_query = "SELECT id_producto, nombre, descripcion, precio, imagen, id_categoria FROM trabajos"
    with conexion.cursor() as cursor:
        cursor.execute(sql_query)
        trabajos = cursor.fetchall()
    conexion.close()
    return trabajos

def eliminar_trabajo(id):
    conexion = obtener_conexion()
    sql_query = "DELETE FROM trabajos WHERE id_producto = %s"
    with conexion.cursor() as cursor:
        cursor.execute(sql_query, (id,))
    conexion.commit()
    conexion.close()

def obtener_trabajo_por_id(id):
    conexion = obtener_conexion()
    trabajo = None
    sql_query = "SELECT id_producto, nombre, descripcion, precio, imagen, id_categoria FROM trabajos WHERE id_producto = %s"
    with conexion.cursor() as cursor:
        cursor.execute(sql_query, (id,))
        trabajo = cursor.fetchone()
    conexion.close()
    return trabajo

def actualizar_trabajo(nombre, descripcion, precio, id_categoria, path_imagen, id_producto):
    conexion = obtener_conexion()
    sql_query1 = "UPDATE trabajos SET nombre = %s, descripcion = %s, precio = %s, id_categoria = %s WHERE id_producto = %s"
    sql_query2 = "UPDATE trabajos SET nombre = %s, descripcion = %s, precio = %s, id_categoria = %s, imagen = %s WHERE id_producto = %s"
    with conexion.cursor() as cursor:
        if path_imagen == None:
            cursor.execute(sql_query1, (nombre, descripcion, precio, id_categoria, id_producto))
        else:
            cursor.execute(sql_query2, (nombre, descripcion, precio, id_categoria, path_imagen, id_producto))
    conexion.commit()
    conexion.close()
"""
def login(nombre, contraseña):
    #usuario = []
    conexion = obtener_conexion()
    sql_query = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
    #usuario = cursor.fetchone()
    with conexion.cursor() as cursor:
        cursor.execute(sql_query, (nombre, contraseña))
    conexion.commit()
    conexion.close()
"""

