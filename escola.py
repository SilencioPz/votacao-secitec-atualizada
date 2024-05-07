from flask import Flask, render_template, request, redirect, url_for

class Aluno:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.uf = email
aluno1 = Aluno('Fabiano','66999537642','fabianotaguchi@gmail.com')
lista = [aluno1]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Listagem de alunos', alunos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Cadastro de aluno')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    email = request. form['email']
    telefone = request. form['telefone']
    aluno = Aluno(nome, telefone, email)
    lista.append(aluno)
    return redirect(url_for('index'))

app.run(debug=True)


