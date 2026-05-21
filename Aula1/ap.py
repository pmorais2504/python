# filepath: /h:/PYTHON/PyhonGit/python-tecTI/flask/aula1/ap.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def explain_decorator():
    return """
    <h1>O que é um Decorator em Python?</h1>
    <p>Um decorator em Python é uma função que recebe outra função como entrada e retorna uma nova função com funcionalidades adicionais. 
    Ele é usado para modificar ou estender o comportamento de funções ou métodos sem alterar diretamente o código original.</p>
    
    <h2>Para que ele serve?</h2>
    <p>Decorators são úteis para reutilizar código, adicionar funcionalidades como autenticação, logging, ou validação, 
    e para manter o código mais limpo e organizado.</p>
    
    <h2>Como ele é utilizado no Flask?</h2>
    <p>No Flask, decorators são usados para associar funções Python a rotas específicas. Por exemplo, o decorator <code>@app.route</code> 
    é usado para definir a URL que acionará uma função específica. Veja o exemplo abaixo:</p>
    <pre>
    @app.route('/exemplo')
    def exemplo():
        return "Esta é uma rota de exemplo."
    </pre>
    """

if __name__ == '__main__':
    app.run(debug=True)
