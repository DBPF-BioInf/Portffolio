from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/baixar_curriculo')
def baixar_curriculo():
    return send_file('static/curriculo_Daniel_Barbosa.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) #noqa

