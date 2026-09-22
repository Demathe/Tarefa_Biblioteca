
import sqlite3


nome = input("Nome de usuário?: ")

usuario = { "nome" : nome}


conn = sqlite3.connect("biblioteca.db")


conn.execute("DROP TABLE IF EXISTS usuarios")

conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

conn.execute("INSERT INTO usuarios (nome) VALUES(?)",
                 [(usuario["nome"])])

conn.commit()