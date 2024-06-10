from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

#Criação da aplicação baseada no Flask
app = Flask(__name__)
#Realiza a conexão com o banco de dados
app.config.from_pyfile('configuracao.py')
csrf = CSRFProtect(app)

db = SQLAlchemy(app)
from rotas import *

class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

#Execução da aplicação
if __name__ == '__main__':
    app.run(debug=True)


