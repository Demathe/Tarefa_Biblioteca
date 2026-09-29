import sqlite3

conn = sqlite3.connect(biblioteca.db)

conn.execute("DROP TABLE IF EXISTS emprestimos")

conn.execute("CREATE TABLE emprestimos\
              (id INTEGER PRIMARY KEY AUTOINCREMENT,\
              data TIMESTAMP,\
              usuario_id INTEGER REFERENCES usuarios(id) )")

