from flask import Flask, render_template

# Inicializamos la aplicación
app = Flask(__name__)


# Ruta 1: Devuelve un HTML muy básico
@app.route("/")
def home():
    #    return """
    #        <h1>¡Hola desde Flask en Docker!!!!</h1>
    #        <p>Este es tu primer servidor Python funcionando.</p>
    #    """
    return render_template("index.html")


@app.route("/saludo")
def saludo():
    return "<h1>Bienvenido a Flask</h1>"


@app.route("/saludo/<name>")
def mostrar_saludo(name):
    return render_template("greetings.html", name_greetings=name)


@app.route("/multiplicar/<int:n1>/<int:n2>")
def multiplicar(n1, n2):
    return f"<p>La multiplicación de {n1} x {n2} es de {n1 * n2}</p>"


@app.route("/catalogo/<int:id_product>")
def catalogo(id_product):
    products = [
        {"nombre": "Teclado Mecánico", "precio": 49.99, "disponible": True},
        {"nombre": "Ratón Óptico", "precio": 19.99, "disponible": False},
        {"nombre": "Monitor 4K", "precio": 299.99, "disponible": True},
    ]
    return render_template(
        "catalogo.html", nombre="algo", id_product=id_product, lista_products=products
    )


if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
