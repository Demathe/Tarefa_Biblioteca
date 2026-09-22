import sqlite3




conn = sqlite3.connect("biblioteca.db")


conn.execute("DROP TABLE IF EXISTS autores")

conn.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")


def adicionar_autor():

        
    nome_a = input("Nome do(s) autor(es): ")
    
    autor = { 'nome_a': nome_a}


    conn.execute("INSERT INTO autores (nome) VALUES(?)",
                 [(autor["nome_a"])])

    conn.commit()