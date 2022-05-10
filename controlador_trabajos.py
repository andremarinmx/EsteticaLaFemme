from database.db import obtener_conexion

def insertar_trabajo(nombre, descripcion, precio, path_imagen):
    conexion = obtener_conexion()
    sql_query = "INSERT INTO trabajos(nombre, descripcion, precio, imagen) VALUES (%s, %s, %s, %s)"
    with conexion.cursor() as cursor:
        cursor.execute(sql_query,(nombre, descripcion, precio, path_imagen))
    conexion.commit()
    conexion.close()

def obtener_trabajos():
    conexion = obtener_conexion()
    trabajos = []
    sql_query = "SELECT id, nombre, descripcion, precio, imagen FROM trabajos"
    with conexion.cursor() as cursor:
        cursor.execute(sql_query)
        trabajos = cursor.fetchall()
    conexion.close()
    return trabajos

def eliminar_trabajo(id):
    conexion = obtener_conexion()
    sql_query = "DELETE FROM trabajos WHERE id = %s"
    with conexion.cursor() as cursor:
        cursor.execute(sql_query, (id,))
    conexion.commit()
    conexion.close()

def obtener_trabajo_por_id(id):
    conexion = obtener_conexion()
    trabajo = None
    sql_query = "SELECT id, nombre, descripcion, precio, imagen FROM trabajos WHERE id = %s"
    with conexion.cursor() as cursor:
        cursor.execute(sql_query, (id,))
        trabajo = cursor.fetchone()
    conexion.close()
    return trabajo

def actualizar_trabajo(nombre, descripcion, precio, id):
#def actualizar_trabajo(nombre, descripcion, precio, id, path_imagen):
    conexion = obtener_conexion()
    #sql_query = "UPDATE trabajos SET nombre = %s, descripcion = %s, precio = %s, imagen = %s WHERE id = %s"
    sql_query = "UPDATE trabajos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s"
    with conexion.cursor() as cursor:
        #cursor.execute(sql_query, (nombre, descripcion, precio, id, path_imagen))
        cursor.execute(sql_query, (nombre, descripcion, precio, id))
    conexion.commit()
    conexion.close()