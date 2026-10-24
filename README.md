
# Sistema de Controle de Tarefas

Este projeto foi desenvolvido com o objetivo de colocar em prática meus conhecimentos em **banco de dados, operações CRUD e integração entre frontend e backend**.

A aplicação consiste em um sistema simples de gerenciamento de tarefas, permitindo cadastrar, visualizar, concluir e excluir registros.

Durante o desenvolvimento, pratiquei consultas SQL, integração com MySQL, criação de rotas utilizando Python e Flask e construção de uma interface com HTML, CSS e JavaScript.

## Funcionalidades

- Cadastrar tarefas com título, descrição e prioridade
- Visualizar as tarefas cadastradas
- Marcar tarefas como concluídas
- Excluir tarefas
- Armazenar os registros em um banco de dados MySQL

## Tecnologias utilizadas

- **Python:** desenvolvimento do backend
- **Flask:** criação das rotas e da API
- **MySQL:** armazenamento e gerenciamento dos dados
- **HTML:** estrutura da interface
- **CSS:** estilização
- **JavaScript:** interação com a aplicação

## Estrutura do projeto

```text
controle-tarefas-sql/
├── app.py
├── database.sql
├── index.html
├── script.js
├── style.css
└── README.md
```

## Como executar

### 1. Preparar o ambiente

Para executar o projeto localmente, é necessário ter Python e MySQL instalados.

### 2. Instalar as dependências

No terminal, execute:

```bash
pip install flask mysql-connector-python python-dotenv
```

### 3. Configurar o banco de dados

Execute o arquivo `database.sql` no MySQL para criar o banco `tarefas_db` e as tabelas necessárias.

O banco possui duas tabelas:

- `usuarios`: armazena informações dos usuários.
- `tarefas`: armazena os registros das tarefas e seus respectivos status.

### 4. Configurar a conexão

Crie um arquivo `.env` na pasta do projeto com as informações de conexão do seu MySQL:

```env
DB_HOST=localhost
DB_NAME=tarefas_db
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

Substitua os valores pelas configurações do seu ambiente.

**Importante:** o arquivo `.env` contém informações locais de acesso ao banco e não deve ser publicado no GitHub.

### 5. Executar a aplicação

No terminal, execute:

```bash
python app.py
```

Com o servidor iniciado, acesse:

**Interface da aplicação:**

http://127.0.0.1:5000/

**API de tarefas:**

http://127.0.0.1:5000/tarefas

## Operações CRUD

O projeto utiliza operações básicas de gerenciamento de dados:

| Operação | Método HTTP | Funcionalidade |
|----------|-------------|----------------|
| Create | POST | Cadastrar tarefas |
| Read | GET | Listar tarefas |
| Update | PUT | Marcar tarefas como concluídas |
| Delete | DELETE | Excluir tarefas |

As operações são realizadas por meio da API Flask, com os dados armazenados no MySQL.

## Aprendizados

O desenvolvimento deste projeto permitiu praticar:

- Criação e relacionamento de tabelas em banco de dados relacional
- Consultas e manipulação de dados utilizando SQL
- Implementação de operações CRUD
- Desenvolvimento de rotas com Flask
- Integração entre frontend, backend e banco de dados
- Utilização de requisições HTTP e dados em formato JSON

Este é um projeto de estudos, desenvolvido para consolidar conhecimentos fundamentais de desenvolvimento web e banco de dados.
