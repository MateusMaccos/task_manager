# Projeto Django - Gerenciador de Tarefas

Este projeto é um gerenciador de tarefas desenvolvido em Django. Ele permite que os usuários façam login, criem, editem e excluam tarefas, além de marcar tarefas como concluídas.

## 🚀 Tecnologias Utilizadas
- Python 3.10+
- Django 5.1+
- SQLite (banco de dados padrão)
- Bootstrap 5 (para estilização)

---

## Funcionalidades
- CRUD de Tarefas
- Login, Cadastro e Logout de Usuários
- Tarefas filtradas por título e status
- Tarefas únicas dos usuários

---

## 📥 Clonando e Configurando o Projeto

### 1️⃣ Clonar o repositório

```bash
# No terminal, execute o seguinte comando:
git clone https://github.com/SEU_USUARIO/gerenciador-tarefas.git

# Acesse a pasta do projeto
cd gerenciador-tarefas
```

### 2️⃣ Criar e ativar um ambiente virtual

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate

# No macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Instalar as dependências do projeto

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar as migrações do banco de dados

```bash
python manage.py migrate
```

### 5️⃣ Criar um superusuário

```bash
python manage.py createsuperuser
```
Digite um nome de usuário, e-mail e senha para acessar o painel administrativo.

### 6️⃣ Iniciar o servidor local

```bash
python manage.py runserver
```
O projeto estará rodando em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠 Testando a Aplicação

1. Acesse o painel administrativo: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
2. Faça login com o superusuário criado.
3. Teste a criação, edição e exclusão de tarefas.

Caso precise de mais informações, sinta-se à vontade para contribuir ou abrir uma issue no repositório!

---
