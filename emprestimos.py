import datetime
import sqlite3

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS emprestimos")

conn.execute("CREATE TABLE emprestimos\
              (id INTEGER PRIMARY KEY AUTOINCREMENT,\
              data DATE,\
              usuario_id INTEGER REFERENCES usuarios(id) )")

def emprestimo():
    data_string = input("Data do emprestimo(dia/mês/ano): ")
    usuario_id = input("Id do usuario: ")

    objeto_data = datetime.strptime(data_string, "%d/%m/%Y")
    
    conn.execute(f"INSERT INTO emprestimos(data, usuario_id) VALUES('{objeto_data.isoformat()}', {usuario_id})")
    conn.commit()