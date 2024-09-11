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

#Adicionando Produto ->

#conn = sqlite3.connect('exemplo.db')
#cursor = conn.cursor()

#novo_produto = ('Camiseta', 29.99, 50)

#inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

#cursor.execute(inserir_produto, novo_produto)

#conn.commit()

#conn.close()

#Encerrando conexão

#Visualizar Produto ->

conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

selecionar_produtos = "SELECT * FROM Produtos"

cursor.execute(selecionar_produtos)
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)

conn.close()

#Atualizar Produto -> 

conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

novo_preco = 24.99
produto_id = 1

atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"

cursor.execute(atualizar_preco, (novo_preco, produto_id))

conn.commit()

conn.close()