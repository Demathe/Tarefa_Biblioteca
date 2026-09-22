import sqlite3

conn = sqlite3.connect(biblioteca.db)

conn.execute("DROP TABLE IF EXISTS livros")

conn.execute("CREATE TABLE livros(\
    id INTEGER PRIMARY KEY AUTOINCREMENT, \
    id_autor INTEGER REFERENCES autores(id),\
    id_autor INTEGER REFERENCES editoras(id),\
    ano_publicacao INTEGER NOT NULL,\
    edicao INTEGER DEFAULT(1),\
    DISPONIVEL ")