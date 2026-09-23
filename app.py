from flask import Flask, redirect, render_template, request, url_for
import mysql.connector

app = Flask(__name__)


def conexion_db():
    return mysql.connector.connect(
        host="localhost",
        user="incidencias",
        password="incidencias",
        database="incidencias",
    )


@app.route("/", methods=["GET", "POST"])
def inicio():
    conexion = conexion_db()
    cursor = conexion.cursor(dictionary=True)

    # 1. Si el usuario envía el formulario (POST), guardamos en MySQL
    if request.method == "POST":
        aula = request.form.get("aula")
        usuario = request.form.get("usuario")
        descripcion = request.form.get("descripcion")

        if aula and usuario and descripcion:
            sql = "INSERT INTO incidencias (aula, usuario, descripcion) VALUES (%s, %s, %s)"
            cursor.execute(sql, (aula, usuario, descripcion))
            conexion.commit()

        cursor.close()
        conexion.close()
        return redirect(url_for("inicio"))

    # 2. Si solo entra a la web (GET), leemos todas las incidencias de MySQL
    cursor.execute("SELECT * FROM incidencias ORDER BY id DESC")
    lista_incidencias = cursor.fetchall()
    cursor.close()
    conexion.close()

    return render_template("index.html", incidencias=lista_incidencias)


# 3. Ruta para que funcione el botón rojo "Eliminar"
@app.route("/eliminar/<int:id>")
def eliminar(id):
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM incidencias WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)