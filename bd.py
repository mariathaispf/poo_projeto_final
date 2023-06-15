# importando sqlite3
import sqlite3 as lite

# criando e conectando com o banco de dados
con = lite.connect('todo.db')

# Criar tabela
with con:
    cur = con.cursor()
    cur.execute( "CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
"""
# Criar tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")
"""
# Inserir tarefas
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO tarefa(nome) VALUES('Assistir One Piece')")
    cur.execute("INSERT INTO tarefa(nome) VALUES('Comer')")
    cur.execute("INSERT INTO tarefa(nome) VALUES('Jogar Bola')")
    cur.execute("INSERT INTO tarefa(nome) VALUES('Dormir')")
    
# Inserir tarefas
def inserir(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO tarefa (nome) VALUES (?)"
        cur.execute(query, i)
        
# Selecionar tarefas
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tarefa")
    rows = cur.fetchall()
    for row in rows:
        print(row)
# Selecionar tarefas
def selecionar():
    lista_tarefas = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tarefa")
        rows = cur.fetchall()
        for row in rows:
            lista_tarefas.append(row)
    return lista_tarefas
# Deletar tarefas
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM tarefa WHERE id = 3")

# Deletar tarefas
def deletar(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM tarefa WHERE id=?"
        cur.execute(query, i)
# Atualizar tarefas
with con:
    cur = con.cursor()
    cur.execute("UPDATE tarefa SET nome='fazer leitura' WHERE id=2")
# Atualizar tarefas
def atualizar(i):
    with con:
        cur = con.cursor()
        query = "UPDATE tarefa SET nome=? WHERE id=?"
        cur.execute(query, i)