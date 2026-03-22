from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tarefas_db"
)

cursor = conexao.cursor(dictionary=True)

# LISTAR
@app.route("/tarefas", methods=["GET"])
def listar():
    cursor.execute("SELECT * FROM tarefas")
    return jsonify(cursor.fetchall())

# CRIAR
@app.route("/tarefas", methods=["POST"])
def criar():
    dados = request.json

    sql = """
    INSERT INTO tarefas (titulo, descricao, prioridade, usuario_id)
    VALUES (%s, %s, %s, %s)
    """

    valores = (
        dados["titulo"],
        dados["descricao"],
        dados.get("prioridade", "media"),
        dados.get("usuario_id", 1)
    )

    cursor.execute(sql, valores)
    conexao.commit()

    return jsonify({"msg": "Tarefa criada"})

# ATUALIZAR STATUS
@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):
    cursor.execute("""
        UPDATE tarefas 
        SET status='concluido', data_conclusao=NOW() 
        WHERE id=%s
    """, (id,))
    conexao.commit()

    return jsonify({"msg": "Tarefa concluída"})

# DELETAR
@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar(id):
    cursor.execute("DELETE FROM tarefas WHERE id=%s", (id,))
    conexao.commit()

    return jsonify({"msg": "Tarefa removida"})

if __name__ == "__main__":
    app.run(debug=True)
