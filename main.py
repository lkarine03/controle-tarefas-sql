import sqlite3

# Conectar ao banco
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conn.commit()

def adicionar_tarefa():
    descricao = input("Digite a tarefa: ")
    cursor.execute("INSERT INTO tarefas (descricao, status) VALUES (?, ?)", (descricao, "pendente"))
    conn.commit()
    print("Tarefa adicionada!\n")

def listar_tarefas():
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa encontrada.\n")
        return

    for tarefa in tarefas:
        print(f"[{tarefa[0]}] {tarefa[1]} - {tarefa[2]}")
    print()

def concluir_tarefa():
    id_tarefa = input("Digite o ID da tarefa: ")
    cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = ?", (id_tarefa,))
    conn.commit()
    print("Tarefa concluída!\n")

def remover_tarefa():
    id_tarefa = input("Digite o ID da tarefa: ")
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    print("Tarefa removida!\n")

def menu():
    while True:
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

menu()

conn.close()
