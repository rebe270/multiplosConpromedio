from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def multiplos_cuatro_cifras(dia):
    multiplos = []
    num = 1000
    while len(multiplos) < 3:
        if num % dia == 0:
            multiplos.append(num)
        num += 1
    return multiplos

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

@app.route("/")
def index():
    dia_actual = datetime.now().day
    multiplos = multiplos_cuatro_cifras(dia_actual)
    promedio = calcular_promedio(multiplos)
    return render_template("index.html", dia_actual=dia_actual, multiplos=multiplos, promedio=promedio)

if __name__ == "__main__":
    app.run(debug=True)
