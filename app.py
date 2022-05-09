from flask import Flask, render_template, request, redirect
import controlador_trabajos

app = Flask(__name__)

@app.route("/")
@app.route("/trabajos")
def trabajos():
    trabajos = controlador_trabajos.obtener_trabajos()
    return render_template("trabajos.html", trabajos=trabajos)

@app.route("/agregar_trabajo")
def formulario_agregar_trabajo():
    return render_template("agregar_trabajo.html")

@app.route("/guardar_trabajo", methods=["POST"])
def guardar_trabajo():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    #imagen = request.form["imagen"]
    #controlador_trabajos.insertar_trabajo(nombre, descripcion, precio, imagen)
    controlador_trabajos.insertar_trabajo(nombre, descripcion, precio)

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
    id = request.form["id"]
    request.files
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    #imagen = request.form["imagen"]
    #controlador_trabajos.actualizar_trabajo(nombre, descripcion, precio, id, imagen)
    controlador_trabajos.actualizar_trabajo(nombre, descripcion, precio, id)
    return redirect("/trabajos")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)