
# 📌 Projeto Pinterest Clone

Este é um projeto de clone simplificado do Pinterest, desenvolvido em **Python** com o framework **Flask**. Ele permite aos usuários se cadastrarem, fazerem login, postar imagens e visualizar um feed com as imagens publicadas.

## 🚀 Funcionalidades

- Cadastro e login de usuários
- Publicação de imagens com descrição
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
git clone https://github.com/seu-usuario/pinterest-clone.git
cd pinterest-clone
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

4. Execute o projeto:

```bash
python main.py
```

5. Acesse no navegador:

```
http://localhost:5000
```

## ✅ Requisitos do `requirements.txt`

Seu projeto depende principalmente dos seguintes pacotes:

- Flask
- Flask-SQLAlchemy
- Flask-Migrate

> Todos os pacotes estão listados no arquivo `requirements.txt`

## 📌 Observações

- As imagens postadas são salvas localmente em `static/imagens`.
- O projeto usa um banco SQLite (`app.db`), ideal para ambientes de teste e desenvolvimento.

---

## 📬 Contato

Caso tenha dúvidas ou sugestões, entre em contato pelo GitHub ou abra uma *issue*.

---
