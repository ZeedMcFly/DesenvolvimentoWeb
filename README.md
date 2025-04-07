
# 📌 Projeto Pinterest Clone

Este é um projeto de clone simplificado do Pinterest, desenvolvido em **Python** com o framework **Flask**. Ele permite aos usuários se cadastrarem, fazerem login, postar imagens e visualizar um feed com as imagens publicadas.

## 🚀 Funcionalidades

- Cadastro e login de usuários
- Publicação de imagens
- Visualização de imagens em um feed
- Listagem de usuários
- Upload e armazenamento local de imagens

## 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- Jinja2 (templates)
- SQLite (banco de dados)
- SQLAlchemy (ORM)
- Flask-Migrate (migrações)
- Bootstrap (estilização)
- HTML/CSS

## 📁 Estrutura do Projeto

```
Pinterest/
├── app/
│   ├── __init__.py            # Inicialização da aplicação Flask
│   ├── models.py              # Modelos de banco de dados com SQLAlchemy
│   └── routes.py              # Rotas principais da aplicação
├── instance/
│   └── config.py              # Configurações da aplicação (ex: SECRET_KEY)
├── migrations/                # Arquivos de migração do banco (gerado pelo Flask-Migrate)
├── static/
│   └── imagens/               # Armazenamento local das imagens postadas
├── templates/
│   ├── cadastro.html          # Tela de cadastro
│   ├── login.html             # Tela de login
│   ├── feed.html              # Tela do feed principal
│   ├── postar.html            # Tela de postagem de imagem
│   └── usuarios.html          # Lista de usuários
├── app.db                     # Banco de dados SQLite
├── main.py                    # Ponto de entrada da aplicação
└── requirements.txt           # Dependências do projeto
```

## ⚙️ Como Rodar o Projeto

### Pré-requisitos

- Python 3 instalado
- pip instalado

### Passos

1. Clone este repositório:

```bash
git clone https://github.com/ZeedMcFly/DesenvolvimentoWeb.git
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o banco de dados:

```bash
python criar_banco.py
```

5. Execute o projeto:

```bash
python main.py
```

6. Acesse no navegador:

```
http://localhost:5000
```

##  Autor  

 **Desenvolvido por Luiz da Silva Oliveira (ZeedMcFly)**  
clone do site Pinterest
