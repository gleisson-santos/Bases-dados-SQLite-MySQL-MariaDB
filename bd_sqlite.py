import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
#Modo 1
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Gleisson", 80.5)')

#Modo 2
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))

#Modo 3
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {'nome': 'Joãozinho', 'peso': 25})

#Modo 4
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {'id': None, 'nome': 'Daniel', 'peso': 113})

# conexao.commit()

#Modo UPDATE
# ATUALIZANDO DADOS PELO ID
cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Xerife', 'id':1}
)
conexao.commit()

#Modo DELETE
# EXCLUINDO DADOS
# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 9}
# )
# conexao.commit()


cursor.execute('SELECT id, nome, peso FROM clientes WHERE peso > 50')

for linha in cursor.fetchall():
    # nome, peso = linha
    # print(nome, peso)
    print(linha)


cursor.close()
conexao.close()
