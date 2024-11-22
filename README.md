# SupGuard - Sistema CRUD com Flask, React e PostgreSQL

## Pré-requisitos

Certifique-se de que você possui as seguintes ferramentas instaladas no seu ambiente:

1. *Python 3.12.7*  
   - [Download Python](https://www.python.org/downloads/)
   - Verifique com o pip se a versão instalada é a correta:  
     ```bash
     pip --version
     ```

2. *Node.js 16 ou superior*  
   - [Download Node.js](https://nodejs.org/)
   - Verifique a instalação:  
     ```bash
     node --version
     npm --version
     ```

3. *PostgreSQL*  
   - [Download PostgreSQL](https://www.postgresql.org/download/)  
   - Por meio do PgAdmin, crie um banco de dados de nome supguard_banco.  

4. *Visual Studio Code* (ou seu editor de preferência)  
   - [Download VS Code](https://code.visualstudio.com/)

---

## Passo a Passo para Configuração

### 1. Backend (Flask)

1. Navegue até a pasta do backend no terminal.
2. Crie e ative um ambiente virtual: 
   - No Linux/macOS:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
     
   - No Windows:
     ```bash
     python -m venv venv
     .venv\Scripts\activate
     ```
     
3. Instale as dependências do Python:
   ```bash
   pip install flask flask-sqlalchemy flask-cors flask-bcrypt psycopg2
   ```

Certifique-se de que o PostgreSQL está rodando e ajuste as configurações de banco de dados no arquivo do backend, se necessário.

Nevegue até o cd backend:
Rode o script para criar as tabelas no banco de dados:
```bash
python create_db.py
```


### 2. Frontend (React):
Navegue até a pasta do frontend no terminal.
Instale as dependências do React:
```bash
npm install
```

Executando o Projeto:
Iniciar o backend:
No terminal, rode:

```bash
python app.py
```


Iniciar o frontend:
Abra um novo terminal, navegue até a pasta frontend e rode:

```bash
npm start
```

Acesse o frontend no navegador em:
http://localhost:3000

O backend estará rodando em:
http://localhost:5000

Observação
Certifique-se de que o PostgreSQL está rodando antes de iniciar o backend.
