import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, g, jsonify, request, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)


def obter_conexao():
    """Cria uma conexao por requisicao, quando necessaria."""
    if "conexao" not in g:
        app_db_user = os.getenv("DB_USER")
        if not app_db_user:
            raise RuntimeError("Configure DB_USER no arquivo .env")
        g.conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=app_db_user,
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "tarefas_db"),
        )
    return g.conexao


@app.teardown_appcontext
def fechar_conexao(erro=None):
    conexao = g.pop("conexao", None)
    if conexao is not None:
        conexao.close()


@app.errorhandler(mysql.connector.Error)
def erro_banco(exc):
    app.logger.exception("Erro ao acessar o banco de dados")
    return jsonify({"erro": "Não foi possível acessar o banco de dados."}), 500


@app.errorhandler(RuntimeError)
def erro_configuracao(exc):
    app.logger.exception("Erro de configuração")
    return jsonify({"erro": "Verifique a configuração local da aplicação."}), 500


@app.get("/")
def pagina_inicial():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/style.css")
def arquivo_css():
    return send_from_directory(BASE_DIR, "style.css")


@app.get("/script.js")
def arquivo_js():
    return send_from_directory(BASE_DIR, "script.js")


@app.get("/tarefas")
def listar():
    conexao = obter_conexao()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM tarefas ORDER BY id DESC")
        tarefas = cursor.fetchall()
    finally:
        cursor.close()
    return jsonify(tarefas), 200


@app.post("/tarefas")
def criar():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie um objeto JSON válido."}), 400

    titulo = dados.get("titulo")
    if not isinstance(titulo, str) or not titulo.strip():
        return jsonify({"erro": "O título é obrigatório."}), 400
    titulo = titulo.strip()
    if len(titulo) > 255:
        return jsonify({"erro": "O título deve ter até 255 caracteres."}), 400

    descricao = dados.get("descricao")
    if descricao is not None and not isinstance(descricao, str):
        return jsonify({"erro": "A descrição deve ser um texto."}), 400

    prioridade = dados.get("prioridade", "media")
    if prioridade not in ("baixa", "media", "alta"):
        return jsonify({"erro": "Prioridade inválida."}), 400

    # O banco permite NULL. Não exigimos um usuário inexistente de ID 1.
