
# Sistema de Controle de Tarefas

Aplicação web desenvolvida para gerenciamento de tarefas, utilizando Python, Flask e MySQL no backend, com interface em HTML, CSS e JavaScript.

O projeto foi criado para praticar o desenvolvimento de APIs REST, a integração entre frontend e backend e a persistência de informações em um banco de dados relacional.

## Sobre o projeto

O sistema permite cadastrar, visualizar, concluir e excluir tarefas por meio de uma interface web conectada a uma API Flask.

As informações são armazenadas em um banco de dados MySQL, permitindo a persistência das tarefas cadastradas.

## Funcionalidades

- Cadastrar tarefas com título, descrição e prioridade
- Listar tarefas cadastradas
- Marcar tarefas como concluídas
- Registrar a data de conclusão
- Excluir tarefas
- Armazenar informações em banco de dados relacional
- Validar os dados enviados à API

## Tecnologias utilizadas

**Backend**
- Python
- Flask
- MySQL
- MySQL Connector/Python

**Frontend**
- HTML
- CSS
- JavaScript

**Outras ferramentas**
- Git e GitHub
- Variáveis de ambiente para configuração do banco de dados

## Estrutura do projeto

```text
controle-tarefas-sql/
├── app.py
├── database.sql
├── index.html
├── style.css
├── script.js
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

O arquivo `app.py` contém a API Flask e disponibiliza os arquivos da interface web. O arquivo `database.sql` contém a estrutura das tabelas utilizadas pela aplicação.

## Como executar o projeto

### 1. Requisitos

Para executar o projeto localmente, é necessário ter instalado:

- Python
- MySQL
- Git (opcional, para clonar o repositório)

### 2. Obter o projeto

Clone o repositório:

```bash
git clone https://github.com/lkarine03/controle-tarefas-sql.git
```

Entre na pasta:

```bash
cd controle-tarefas-sql
```

Também é possível baixar o projeto diretamente pelo GitHub.

### 3. Instalar as dependências

Execute:

```bash
pip install -r requirements.txt
```

As dependências utilizadas são:

- Flask
- mysql-connector-python
- python-dotenv

### 4. Configurar o banco de dados

Inicie o servidor MySQL e execute o arquivo `database.sql` para criar o banco `tarefas_db` e as tabelas necessárias.

O banco utiliza duas tabelas:

**usuarios**
- id
- nome
- email

**tarefas**
- id
- titulo
- descricao
- prioridade
- status
- data_criacao
- data_conclusao
- usuario_id

A tabela `tarefas` possui uma chave estrangeira para a tabela `usuarios`.

O cadastro de tarefas não exige um usuário associado. Caso seja informado um `usuario_id`, ele deverá corresponder a um usuário existente.

### 5. Configurar as variáveis de ambiente

Crie um arquivo chamado `.env` na pasta principal do projeto, utilizando o `.env.example` como referência.

Exemplo:

```env
DB_HOST=localhost
DB_NAME=tarefas_db
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
FLASK_DEBUG=0
```

Substitua os valores pelas configurações do seu MySQL.

O usuário informado precisa ter permissão para consultar, inserir, atualizar e excluir registros nas tabelas do projeto.

**Importante:** o arquivo `.env` contém configurações locais e não deve ser enviado ao GitHub.

### 6. Executar a aplicação

No terminal, execute:

```bash
python app.py
```

Com o servidor iniciado, acesse:

**Interface web:**

http://127.0.0.1:5000/

**API de tarefas:**

http://127.0.0.1:5000/tarefas

O endereço da API retorna as tarefas em formato JSON.

## Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tarefas` | Lista as tarefas cadastradas |
| POST | `/tarefas` | Cadastra uma nova tarefa |
| PUT | `/tarefas/<id>` | Marca uma tarefa como concluída |
| DELETE | `/tarefas/<id>` | Exclui uma tarefa |

### Exemplo de cadastro

Requisição:

```http
POST /tarefas
Content-Type: application/json
```

Corpo da requisição:

```json
{
  "titulo": "Estudar Python",
  "descricao": "Revisar conceitos de Flask",
  "prioridade": "alta"
}
```

Exemplo de resposta:

```json
{
  "msg": "Tarefa criada",
  "id": 1
}
```

O identificador retornado é gerado pelo banco de dados.

### Conclusão de tarefas

Ao utilizar a rota `PUT /tarefas/<id>`, a aplicação altera o status da tarefa para `concluido` e registra sua data de conclusão.

### Exclusão de tarefas

A rota `DELETE /tarefas/<id>` remove a tarefa correspondente do banco de dados.

Quando uma tarefa não é encontrada nas operações de atualização ou exclusão, a API retorna o código HTTP `404`.

## Organização e boas práticas

A aplicação utiliza:

- Consultas SQL parametrizadas
- Validação de informações recebidas pela API
- Tratamento de erros de banco de dados
- Gerenciamento de conexões com o MySQL
- Configurações de acesso por variáveis de ambiente
- Códigos de resposta HTTP apropriados

O projeto foi desenvolvido para fins de estudo e execução em ambiente local. Não possui autenticação de usuários e não está preparado para exposição pública sem controles adicionais de segurança.

## Demonstração

As capturas de tela da interface e do funcionamento da aplicação serão adicionadas ao repositório.

## Aprendizados

O desenvolvimento deste projeto permitiu praticar conceitos de:

- Desenvolvimento de APIs REST com Flask
- Integração entre frontend e backend
- Operações CRUD
- Modelagem e consultas em banco de dados relacional
- Requisições HTTP e manipulação de JSON
- Organização de código e tratamento de erros
- Configuração de aplicações com variáveis de ambiente

