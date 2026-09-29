import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS livros")

conn.execute("""CREATE TABLE livros(\
    id INTEGER PRIMARY KEY AUTOINCREMENT, \
    id_autor INTEGER REFERENCES autores(id),\
    id_editora INTEGER REFERENCES editoras(id),\
    ano_publicacao INTEGER NOT NULL,\
    edicao INTEGER DEFAULT(1),\
    disponivel VARCHAR(4) DEFAULT('SIM'))""")

def adicionar_livro():
    nome = input("Nome do livro: ")
    id_editora = input("Id da editora: ")
    autor_id = input("Id do autor: ")
    ano_publicacao = input("Ano de publicação: ")
    edicao = input("Edição do livro: ")
    
    
    #adiciona só um por vez
    conn.execute(f"INSERT INTO livros(titulo, autor_id, editora_id, ano_publicacao, edicao,\
                    disponivel) VALUES({nome, id_editora, autor_id, ano_publicacao, edicao})")

    conn.commit()


