import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Nome do arquivo onde os dados serão salvos
ARQUIVO_DADOS = 'clientes.json'

# Função para carregar clientes a partir de um arquivo JSON
def carregar_clientes():
    """Lê a lista de clientes salva no arquivo JSON."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Função para salvar clientes em um arquivo JSON
def salvar_clientes(clientes):
    """Salva a lista de clientes no arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

"""
    Rota principal da aplicação, carrega e renderiza a página inicial HTML, juntamente com a lista de clientes cadastrados.
"""
@app.route('/')
def index():
    """Página principal: exibe a lista de clientes cadastrados."""
    clientes = carregar_clientes()
    return render_template('index.html', clientes=clientes)

""""
    Rota para cadastrar um novo cliente. Recebe os dados do formulário, cria um dicionário com as informações e salva no arquivo JSON.
"""
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    """Recebe os dados do formulário e salva o novo cliente."""
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    saldo = request.form.get('saldo', 0)

    # Converte o saldo digitado para número decimal
    try:
        saldo_float = float(saldo)
    except ValueError:
        saldo_float = 0.0

    # Cria o dicionário do novo cliente
    novo_cliente = {
        'nome': nome,
        'cpf': cpf,
        'saldo': saldo_float
    }

    # Carrega a lista atual, adiciona o novo cliente e salva no arquivo
    clientes = carregar_clientes()
    clientes.append(novo_cliente)
    salvar_clientes(clientes)

    # Redireciona para a página principal atualizada
    return redirect(url_for('index'))

"""
    Rota para deletar um cliente existente. Recebe o CPF do cliente a ser removido, filtra a lista de clientes e salva a lista atualizada no arquivo JSON.
"""
@app.route('/deletar/<cpf>', methods=['POST'])
def deletar(cpf):
    """Remove um cliente existente buscando pelo CPF."""
    clientes = carregar_clientes()
    # Mantém apenas os clientes cujo CPF seja diferente do informado
    clientes = [c for c in clientes if c.get('cpf') != cpf]
    salvar_clientes(clientes)

    return redirect(url_for('index'))


if __name__ == '__main__':
    print("Servidor iniciado em http://127.0.0.1:5000")
    app.run(debug=True)
