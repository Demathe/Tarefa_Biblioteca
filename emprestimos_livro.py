from datetime import datetime
import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS emprestimos_livros")

conn.execute("CREATE TABLE emprestimos_livros(\
    emprestimo_id INTEGER REFERENCES emprestimo(id),\
    livro_id INTEGER REFERENCES livros(id),\
    data_devolucao DATE, \
    PRIMARY KEY (emprestimo_id, livro_id))")


def emprestimo_livro():
    emprestimo_id = input("Id do emprestimo: ")
    livro_id = input("Id do livro: ")
    data_string = input("Data de devolução(dia/mês/ano): ")


    objeto_data = datetime.strptime(data_string, "%d/%m/%Y")
    
    
    conn.execute(F"INSERT INTO emprestimos_livros(emprestimo_id, livro_id, data_devolucao) VALUES({emprestimo_id}, {livro_id}, '{objeto_data.isoformat()}')")
    conn.commit()
