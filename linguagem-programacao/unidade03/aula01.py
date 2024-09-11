import sqlite3

conn = sqlite3.connect('exemplo.db')

cursor = conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS Produtos(
    id  INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
"""

cursor.execute(create_table)

conn.execute(create_table)

conn.commit()