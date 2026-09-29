import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS emprestimos_livros")

conn.execute("CREATE TABLE emprestimos_livros(\
    emprestimo_id INTEGER REFERENCES emprestimo(id),\
    livro_id INTEGER REFERENCES livros(id),\
    data_devolucao DATE, \
    PRIMARY KEY (emprestimo_id, livro_id))")


