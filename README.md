Sistema de Gerenciamento de EPIs

Este projeto foi desenvolvido como atividade prática do curso Desenvolvimento de Sistemas.
O objetivo é criar um sistema web para gerenciar colaboradores, EPIs e empréstimos, permitindo mais organização e segurança no ambiente de trabalho.

🚀 Funcionalidades

Cadastro, edição, listagem e exclusão de Colaboradores

Cadastro, edição, listagem e exclusão de EPIs

Registro de empréstimos de EPIs

Controle de devoluções de EPIs

Dashboard com visão geral do sistema

Autenticação de usuários (login e logout)



🛠️ Tecnologias Utilizadas

Python 3.11+

Django 5.x

SQLite3

HTML + CSS (Bootstrap)

⚙️ Como Rodar o Projeto

Clone este repositório:

git clone https://github.com/SEU_USUARIO/seu_repositorio.git
cd seu_repositorio


Crie e ative um ambiente virtual (Windows):

python -m venv venv
.\venv\Scripts\activate


Ou no Linux/Mac:

python3 -m venv venv
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Realize as migrações:

python manage.py migrate


Crie um superusuário:

python manage.py createsuperuser


Rode o servidor:

python manage.py runserver


Acesse no navegador:

http://127.0.0.1:8000