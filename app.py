from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Currículo</h1>
    <p>Bem-vindo ao meu currículo online!</p>
    <ul>
        <li><a href="/sobre">Sobre Mim</a></li>
        <li><a href="/experiencia">Experiência</a></li>
        <li><a href="/educacao">Educação</a></li>
        <li><a href="/contato">Contato</a></li>
    </ul>
    """

@app.route('/sobre')
def sobre():
    return """
    <h1>Sobre Mim</h1>
    <p>Meu nome é Paulo Vitor Morais de Andrade Resende. Sou um desenvolvedor com experiência em Python e Flask.</p>
    <a href="/">Voltar</a>
    """

@app.route('/experiencia')
def experiencia():
    return """
    <h1>Experiência</h1>
    <ul>
        <li>Desenvolvedor Python na Empresa Cotemig (2020 - Presente)</li>
        <li>Estagiário de TI na Empresa Inter (2018 - 2020)</li>
    </ul>
    <a href="/">Voltar</a>
    """

@app.route('/educacao')
def educacao():
    return """
    <h1>Educação</h1>
    <ul>
        <li>Bacharelado em Ciência da Computação - Universidade faculdade Cotemig (2015 - 2019)</li>
    </ul>
    <a href="/">Voltar</a>
    """

@app.route('/contato')
def contato():
    return """
    <h1>Contato</h1>
    <p>Email: pvmorais2508@gmail.com</p>
    <p>Telefone: (31) 98304-0406</p>
    <a href="/">Voltar</a>
    """

if __name__ == '__main__':
    app.run(debug=True)