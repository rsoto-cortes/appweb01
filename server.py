from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html', title='Home', message='Bienvenido a la pagina de inicio')

@app.route("/servicios")
def servicios():
    return render_template('servicios.html', title='Servicios', message='Bienvenido a la pagina de servicios')

@app.route("/contacto")
def contacto():
    return render_template('contacto.html', title='Contacto', message='Bienvenido a la pagina de contacto')
@app.route("/productos")
def productos():
    return render_template("productos.html", title='Productos', message='Bienvenido a la pagina de productos')

if __name__ == '__main__':
    app.run(debug=True, port=5050)