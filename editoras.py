#adicionar editoras e criar tabela
#lorenzo

import sqlite3


conn = sqlite3.connect("biblioteca.db")

conn.execute("CREATE TABLE editoras (id PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL)")