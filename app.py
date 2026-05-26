from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Chama a função calcular para processar os dados do formulário
        return calcular()
    # Em caso de GET, renderiza o formulário vazio
    return render_template("calculadora.html", etapas="", resultados="")

if __name__ == "__main__":
    app.run(debug=True)