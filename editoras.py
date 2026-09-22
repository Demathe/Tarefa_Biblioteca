#adicionar editoras e criar tabela
#lorenzo

import sqlite3


conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS editoras")

conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome VARCHAR(100) NOT NULL)")


def adicionar_editoar():
    nome = input("Nome da editora: ")
    
    #adiciona só um por vez
    conn.execute(f"INSERT INTO editora(nome) VALUES({nome})")

    conn.commit()