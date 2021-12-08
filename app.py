from flask import Flask, request, session, redirect, url_for, render_template
import re
import datetime
from model.log import *
import secrets
from services.operationsService import *

app = Flask(__name__)

# @app.route('/inicio', methods=['GET', 'POST'])
# def login():
#     msg = ''
#  # conexão do banco
#     conn = mysql.connect()
#     cursor = conn.cursor(pymysql.cursors.DictCursor)

#     # Verifica se requisição POST com campo 'nome' e 'senha' existem:
#     if request.method == 'POST' and 'nome' in request.form and 'senha' in request.form:
#         # Variáveis de fácil acesso
#         nome = request.form['nome']
#         senha = request.form['senha']
#         # Verifica se conta existe no MySQL
#         cursor.execute(
#             'SELECT * FROM usuario WHERE nome = %s AND senha = %s', (nome, senha))
#         usuario = cursor.fetchone()

#     # Se a conta existe no banco de dados:
#         if usuario:
#             # Cria sessão
#             session['loggedin'] = True
#             session['nome'] = usuario['nome']
#             # retorna login com sucesso e redireciona pra página principal
#             return redirect(url_for('home'))
#         else:
#             # Se a conta não existe ou credenciais estão incorretas:
#             msg = 'Credenciais incorretas ou conta não existe.'

#     return render_template('index.html', msg=msg)


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#  # connect
#     conn = mysql.connect()
#     cursor = conn.cursor(pymysql.cursors.DictCursor)

#     # Mensagem se algo errado acontece
#     msg = ''
#     # Verifica se requisição POST com campo 'nome' e 'senha' existem:
#     if request.method == 'POST' and 'nome' in request.form and 'senha' in request.form:
#         # Create variables for easy access
#         nome = request.form['nome']
#         senha = request.form['senha']

#   # Verifica se a conta existe:
#         cursor.execute('SELECT * FROM usuario WHERE nome = %s', (nome))
#         usuario = cursor.fetchone()
#         # Se a conta já existe:
#         if usuario:
#             msg = 'Essa conta já existe!'
#         elif not re.match(r'[A-Za-z0-9]+', nome):
#             msg = 'Nome de usuário deve conter apenas números ou letras'
#         elif not nome or not senha:
#             msg = 'Por favor, complete o formulário!'
#         else:
#             # Conta não existe, então é inserida no banco.
#             cursor.execute('INSERT INTO usuario VALUES (%s, %s)', (nome, senha))
#             conn.commit()
#             msg = 'Registrado com sucesso, agora volte e logue!'
#     elif request.method == 'POST':
#         # Formulário vázio
#         msg = 'Por favor, complete o formulário.'
#     # Mostra mensagem de registro
#     return render_template('register.html', msg=msg)


# @app.route('/')
# def home():
#     return render_template('index.html')
    


#Rota Calculadora
@app.route('/calculadora')
def calculadora():
    return render_template('form.html')
    
#Rota Calculadora Avançada
@app.route('/calculadoraAvancada')
def calculadoraAvancada():
    return render_template('op-transcendentes.html')
    
#Rota do Log
@app.route('/log')
def log():
    return render_template('log.html', operacoes=sessao.query(Log).all())

#Rota do resultado
@app.route('/resultado', methods=['POST'])
def resultado():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operacao = request.form.get("Operação")
    historico = str(var_1) + ', ' + str(var_2)
    data = datetime.datetime.now()
    operacao = request.form.get("Operação")
    entry = elementarFunction(var_1, var_2, operacao)
    addOperacao(entry[1], entry[2], data, historico, entry[0])
    return render_template('resultado.html', entry=entry[0])
   

#Rota do resultado avançado
@app.route('/resultadoAvancado', methods=['POST'])
def resultadoAvancado():
        var_1 = request.form.get("var_1", type=int)
        operacao = request.form.get("Operação")
        historico = str(var_1) 
        data = datetime.datetime.now()
        operacao = request.form.get("Operação")
        entry = transcendentFunction(var_1, operacao)
        addOperacao(entry[1], entry[2], data, historico, entry[0])
        return render_template('resultadoAvancado.html', entry=entry)


if __name__ == '__main__':
    app.run(debug=True)
