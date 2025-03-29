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
git clone https://github.com/SEU_USUARIO/task_manager.git

# Acesse a pasta do projeto
cd task_manager
```

2️⃣ Criar e ativar um ambiente virtual

# Criar o ambiente virtual
```bash
python -m venv venv
```

# Ativar o ambiente virtual
# No Windows:
```bash
venv\Scripts\activate
```

# No macOS/Linux:
```bash
source venv/bin/activate
```

3️⃣ Instalar as dependências do projeto
```bash
pip install -r requirements.txt
```

4️⃣ Configurar as variáveis de ambiente

Crie um arquivo .env na raiz do projeto e adicione o seguinte conteúdo:
```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=*
```
Importante: Nunca compartilhe sua SECRET_KEY publicamente. Para garantir que o arquivo .env não seja enviado ao repositório, adicione-o ao .gitignore.

5️⃣ Aplicar as migrações do banco de dados
```bash
python manage.py migrate
```
6️⃣ Criar um superusuário
```bash
python manage.py createsuperuser
```
Digite um nome de usuário, e-mail e senha para acessar o painel administrativo.

7️⃣ Iniciar o servidor local
```bash
python manage.py runserver
```
O projeto estará rodando em: http://127.0.0.1:8000

## 🛠 Testando a Aplicação

1. Acesse a aplicação: [http://127.0.0.1:8000](http://127.0.0.1:8000)
2. Faça login com o superusuário criado ou cadastre um usuário novo.
3. Teste a criação, edição, exclusão e busca de tarefas.

Caso precise de mais informações, sinta-se à vontade para contribuir ou abrir uma issue no repositório!

---

## 🛠 Imagens

### Login
<img align="center" src="https://github.com/MateusMaccos/task_manager/blob/main/assets/login.png">

### Cadastro
<img align="center" src="https://github.com/MateusMaccos/task_manager/blob/main/assets/cadastro.png">

### Lista de Tasks Vazia
<img align="center" src="https://github.com/MateusMaccos/task_manager/blob/main/assets/tasksVazia.png">

### Nova Task
<img align="center" src="https://github.com/MateusMaccos/task_manager/blob/main/assets/novaTarefa.png">

### Tasks Criadas
<img align="center" src="https://github.com/MateusMaccos/task_manager/blob/main/assets/tasksCriada.png">

### Task Concluída
<img align="center" src="https://github.com/MateusMaccos/task_manager/blob/main/assets/taskConcluida.png">

### Excluir Task
<img align="center" src="https://github.com/MateusMaccos/task_manager/blob/main/assets/excluirTasks.png">
<img align="center" src="https://github.com/MateusMaccos/task_manager/blob/main/assets/excluirTasks.png">


---
