from flask import Flask, make_response, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('index.html')


@app.route("/info")
def limit_page():
    return render_template('info.html')


# configurar lo que va dentro de PORT es súper importante
app.run(host='0.0.0.0',port=os.getenv("PORT", 5000), debug=True)

# PORT será por defecto mi local host 5000 pero con getnv se toma el entorno de la nube si nos asigna 
# un entorno. Ese entorno suistituirá el puerto por defecto 5000 

# Importante es comnprobar que funciona en local antes de subir nada a Heroku.


