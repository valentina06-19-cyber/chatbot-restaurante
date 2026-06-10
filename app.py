from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Asistente Virtual Restaurante</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                text-align: center;
                padding: 40px;
            }

            .contenedor {
                background: white;
                max-width: 700px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
            }

            h1 {
                color: #d35400;
            }

            h2 {
                color: #333;
            }

            ul {
                text-align: left;
                display: inline-block;
            }
        </style>
    </head>

    <body>

        <div class="contenedor">

            <h1>🍽️ Asistente Virtual del Restaurante</h1>

            <h2>Menú Disponible</h2>

            <ul>
                <li>Hamburguesa Artesanal - $12.000</li>
                <li>Sancocho Tradicional - $15.000</li>
                <li>Bandeja Paisa - $20.000</li>
                <li>Jugo Natural - $5.000</li>
            </ul>

            <h2>Promociones</h2>

            <p>✅ 2x1 en hamburguesas los martes</p>
            <p>✅ 20% de descuento para estudiantes</p>
            <p>✅ Bebida gratis en compras superiores a $30.000</p>

            <h2>Estado del Sistema</h2>

            <p>🟢 Chatbot funcionando correctamente.</p>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
