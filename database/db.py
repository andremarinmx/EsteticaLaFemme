import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost', user='root', password='1234', db='LaFemme')
