CREATE DATABASE tarefas_db;

USE tarefas_db;

CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    descricao TEXT,
    status VARCHAR(50) DEFAULT 'pendente'
);
