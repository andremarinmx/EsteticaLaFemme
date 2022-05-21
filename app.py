from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
import controlador_trabajos
import os

app = Flask(__name__)

app.secret_key = "1234567890"
uploads_dir = os.path.join('static/uploads')

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/portafolio")
def portafolio():    
    trabajos = controlador_trabajos.obtener_trabajos()
    return render_template("portafolio.html", trabajos=trabajos)

@app.route("/preguntas")
def preguntas():    
    return render_template("preguntas.html")

@app.route("/trabajos")
def trabajos():
    if "nombre_usuario" in session:
        trabajos = controlador_trabajos.obtener_trabajos()
        return render_template("trabajos.html", trabajos=trabajos)
    else:
        return redirect("/login")

@app.route('/login')
def login():
    return render_template("login.html")
database={'admin':'admin'}

@app.route('/formulario_login',methods=["POST"])
def formulario_login():
    nombre_usuario = request.form['usuario']
    contrasena_usuario = request.form['contrasena']
    session["nombre_usuario"] = nombre_usuario
    session["contrasena_usuario"] = contrasena_usuario
    if nombre_usuario not in database:
        return render_template('login.html',mensaje='Usuario inválido')
    else:
        if database[nombre_usuario]!=contrasena_usuario:
            return render_template('login.html',mensaje='Contraseña inválida')
        else:
            return (redirect("/trabajos"))
    
@app.route("/agregar_trabajo")
def formulario_agregar_trabajo():  
    if "nombre_usuario" in session: 
        return render_template("agregar_trabajo.html")
    else:
        return redirect("/login")

@app.route("/guardar_trabajo", methods=["POST"])
def guardar_trabajo():
    if "nombre_usuario" in session:
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        imagen = request.files["imagen"]
        imagen.save(os.path.join(uploads_dir, secure_filename(imagen.filename)))
        path_imagen = os.path.join(uploads_dir, secure_filename(imagen.filename))
        id_categoria = request.form["categoria"]
        controlador_trabajos.insertar_trabajo(nombre, descripcion, precio, path_imagen, id_categoria)
        return redirect("/trabajos")
    else:
        return redirect("/login")

@app.route("/eliminar_trabajo", methods=["POST"])
def eliminar_trabajo():
    if "nombre_usuario" in session:
        controlador_trabajos.eliminar_trabajo(request.form["id"])
        return redirect("/trabajos")
    else:
        return redirect("/login")

@app.route("/formulario_editar_trabajo/<int:id>")
def editar_trabajo(id):
    if "nombre_usuario" in session:
        trabajo = controlador_trabajos.obtener_trabajo_por_id(id)
        return render_template("editar_trabajo.html", trabajo=trabajo)
    else:
        return redirect("/login")

@app.route("/actualizar_trabajo", methods=["POST"])
def actualizar_trabajo():
    if "nombre_usuario" in session:
        id_producto = request.form["id"]
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        imagen = request.files["imagen"]
        if imagen.filename != "":
            path_imagen = os.path.join(uploads_dir, secure_filename(imagen.filename))
            imagen.save(path_imagen)
        else:
            path_imagen = None
        id_categoria = request.form["categoria"]
        controlador_trabajos.actualizar_trabajo(nombre, descripcion, precio, id_categoria, path_imagen, id_producto)
        return redirect("/trabajos")
    else:
        return redirect("/login")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)