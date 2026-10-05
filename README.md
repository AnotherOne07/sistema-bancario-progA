# 🏦 Sistema Bancário Simples - Exemplo Prático (Programação A)

Este repositório é um exemplo simples de uma aplicação web desenvolvida para os alunos da disciplina de **Programação A**. 

O objetivo é apresentar como criar uma interface web com **HTML** e **CSS** integrada a um backend em **Python (Flask)** que lê e salva dados em um arquivo **JSON**.

---

## 🛠️ Tecnologias Utilizadas

- **HTML**: Cria a estrutura visual da página (formulário de cadastro e tabela de clientes).
- **CSS**: Estiliza os elementos para deixar a página organizada e legível.
- **Python**: Processa as requisições, manipula as listas de dados e grava as informações no arquivo.
- **Flask**: Micro-framework em Python que conecta a página web (HTML) com o código em Python.
- **JSON (`clientes.json`)**: Arquivo de texto simples usado para guardar (persistir) os dados dos clientes.

---

## 🔄 Como as Tecnologias se Comunicam

A comunicação entre a tela e o código Python funciona de forma muito simples:

```text
[ NAVEGADOR (HTML/CSS) ]  <--- (Envia formulário POST) ---  [ SERVIDOR FLASK (Python) ]
           │                                                               │
           └────────────── (Exibe a tabela atualizada) ◄───────────────────┘
                                                                           │
                                                                 (Lê e Salva dados)
                                                                           ▼
                                                                  [ clientes.json ]
```

1. **Leitura de Dados (`GET /`)**: Quando você abre o site no navegador, o Python lê o arquivo `clientes.json` e envia a lista de clientes para a página `index.html`.
2. **Envio de Formulário (`POST /cadastrar`)**: Quando você preenche o formulário e clica em "Salvar Cliente", o navegador envia os dados (Nome, CPF, Saldo) para a rota `/cadastrar` no Python.
3. **Gravação**: O Python adiciona o novo cliente na lista e salva o resultado atualizado no arquivo `clientes.json`.
4. **Atualização**: O Python redireciona a página de volta para a página inicial, exibindo a tabela com o novo cliente cadastrado!

---

## 📂 Estrutura do Projeto

```text
sistema-bancario-progA/
├── app.py                 # Código principal em Python (rotas e leitura/escrita do JSON)
├── clientes.json          # Arquivo simples de armazenamento de dados
├── requirements.txt       # Lista de dependências (Flask)
├── README.md              # Este guia explicativo
├── static/
│   └── css/
│       └── style.css      # Estilos visuais simples
└── templates/
    └── index.html         # Página HTML única com formulário e tabela
```

---

## 💻 Como Preparar o Ambiente e Rodar o Aplicativo

### 0. Pré-requisitos
- Ter o python instalado em sua máquina. Caso não tenha acesse o tutorial abaixo:
- https://python.org.br/instalacao-windows/
- https://python.org.br/instalacao-linux/
- Após realizar a instalação, você pode verificar se ocorreu tudo certo rodando o comando: 
- **Windows**
```powershell
  python --version
```

- **Linux / macOS**
```bash
  python3 --version
```

Siga os passos abaixo no terminal para rodar o projeto no seu computador:

### 1. Criar o Ambiente Virtual (`venv`)

- **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  ```
- **Linux / macOS:**
  ```bash
  python3 -m venv venv
  ```

### 2. Ativar o Ambiente Virtual

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar o Flask

Com o ambiente virtual ativado `(venv)`, execute:
```bash
pip install -r requirements.txt
```
*(Ou diretamente `pip install flask`)*

### 4. Rodar a Aplicação

Execute o arquivo `app.py`:
```bash
python app.py
```

### 5. Abrir no Navegador

Abra o seu navegador e digite o endereço url:
👉 **`http://127.0.0.1:5000`**
