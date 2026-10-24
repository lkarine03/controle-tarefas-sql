# Sistema de Controle de Tarefas

Este é um projeto simples de estudos, criado para colocar em prática meus conhecimentos em **banco de dados, operações CRUD e integração entre frontend e backend**.

A aplicação permite cadastrar, visualizar, marcar como concluídas e excluir tarefas, utilizando Python, Flask e MySQL, com uma interface em HTML, CSS e JavaScript.

## Funcionalidades

- Cadastrar tarefas com título, descrição e prioridade
- Visualizar tarefas cadastradas
- Marcar tarefas como concluídas
- Excluir tarefas
- Armazenar os dados no MySQL
- Exibir mensagens de sucesso ou erro na interface

## Tecnologias

- Python e Flask
- MySQL
- HTML, CSS e JavaScript

## Como executar

1. Instale Python e MySQL e inicie o servidor MySQL.
2. Execute `database.sql` para criar o banco `tarefas_db` e suas tabelas.
3. Instale as dependências:

   ```bash
   python -m pip install flask mysql-connector-python python-dotenv
   ```

4. Configure as variáveis de ambiente do MySQL. Você pode criar um arquivo `.env` **somente no seu computador** (não o publique no GitHub):

   ```env
   DB_HOST=localhost
   DB_NAME=tarefas_db
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   FLASK_DEBUG=0
   ```

   O usuário precisa ter permissões de leitura e escrita no banco. O cadastro de tarefas não exige usuário associado.

5. Inicie o servidor:

   ```bash
   python app.py
   ```

6. Abra a **interface** em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

A rota [http://127.0.0.1:5000/tarefas](http://127.0.0.1:5000/tarefas) retorna os registros em JSON, não a interface visual.

> **Importante:** não abra o `index.html` diretamente pelo Explorador de Arquivos nem pelo GitHub Pages. Neste projeto, a interface deve ser acessada pelo servidor Flask para se comunicar com a API no mesmo endereço.

## Rotas da API

| Método | Rota | Operação |
| --- | --- | --- |
| `GET` | `/tarefas` | Listar tarefas |
| `POST` | `/tarefas` | Cadastrar tarefa |
| `PUT` | `/tarefas/<id>` | Concluir tarefa |
| `DELETE` | `/tarefas/<id>` | Excluir tarefa |

## Aprendizados

O projeto foi desenvolvido para praticar criação de tabelas relacionadas, consultas SQL, operações CRUD, rotas HTTP e comunicação entre frontend, backend e banco de dados.

A aplicação foi pensada para estudos e execução local. Não possui autenticação e não deve ser publicada como serviço aberto na internet sem medidas adicionais de segurança.
