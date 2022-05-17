from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import controlador_trabajos
import os

app = Flask(__name__)

uploads_dir = os.path.join('static/uploads')

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/portafolio")
def portafolio():    
    trabajos = controlador_trabajos.obtener_trabajos()
    return render_template("portafolio.html", trabajos=trabajos)

@app.route("/trabajos")
def trabajos():
    trabajos = controlador_trabajos.obtener_trabajos()
    return render_template("trabajos.html", trabajos=trabajos)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/form_login", methods=["POST, GET"])
def form_login():
    nombre_usuario = request.form["nombre"]
    contraseña_usuario = request.form["contraseña"] 
    print(nombre_usuario)
    print(contraseña_usuario)
    controlador_trabajos.login(nombre_usuario, contraseña_usuario)
    return redirect("/agregar_trabajo")

@app.route("/agregar_trabajo")
def formulario_agregar_trabajo():   
    return render_template("agregar_trabajo.html")

@app.route("/guardar_trabajo", methods=["POST"])
def guardar_trabajo():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    imagen = request.files["imagen"]
    imagen.save(os.path.join(uploads_dir, secure_filename(imagen.filename)))
    path_imagen = os.path.join(uploads_dir, secure_filename(imagen.filename))
    id_categoria = request.form["categoria"]
    controlador_trabajos.insertar_trabajo(nombre, descripcion, precio, path_imagen, id_categoria)
    return redirect("/trabajos")

@app.route("/eliminar_trabajo", methods=["POST"])
def eliminar_trabajo():
    controlador_trabajos.eliminar_trabajo(request.form["id"])
    return redirect("/trabajos")

@app.route("/formulario_editar_trabajo/<int:id>")
def editar_trabajo(id):
    trabajo = controlador_trabajos.obtener_trabajo_por_id(id)
    return render_template("editar_trabajo.html", trabajo=trabajo)

@app.route("/actualizar_trabajo", methods=["POST"])
def actualizar_trabajo():
    id_producto = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    imagen = request.files["imagen"]
    id_categoria = request.form["categoria"]
    imagen.save(os.path.join(uploads_dir, secure_filename(imagen.filename)))
    #path_imagen = os.path.join(uploads_dir, secure_filename(imagen.filename))
    #controlador_trabajos.actualizar_trabajo(nombre, descripcion, precio, id_producto, id_categoria, path_imagen)
    controlador_trabajos.actualizar_trabajo(nombre, descripcion, precio, id_producto, id_categoria)
    return redirect("/trabajos")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)