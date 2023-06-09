import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '12345',
        db = 'clientes',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )


    try:
        yield conexao
    finally:
        print('Fechando a conexão')


with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql =  'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' '(%s, %s, %s, %s)'
        cursor.execute(sql, ('Caio', 'Santos', 110, 200))
        conexao.commit()



with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()


        for linha in resultado:
            print(linha)