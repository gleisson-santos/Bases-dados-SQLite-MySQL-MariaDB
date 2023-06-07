import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '12345',
        #port = '3306',
        db = 'clientes',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()

#Inserir dados
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#         '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()

#Inserir varios dados
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#         '(%s, %s, %s, %s)'

#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROUSE', 'FIGUEIREDO', 19, 55),
#             ('JOSE', 'FIGUEIREDO', 19, 55),
#         ]

#         cursor.executemany(sql, dados)
#         conexao.commit()

#Deletar dados forma 1
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (9,))
#         conexao.commit()

#Deletar dados forma 2
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (10,11,12))
#         conexao.commit()

#Deletar dados forma 3
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (6,8))
#         conexao.commit()
        
#Atualizar dados para um ID
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET sobrenome=%s WHERE id=%s'
#         cursor.execute(sql, ('Meireles', 1))
#         conexao.commit()


# Atualizar dados para vários IDs
dados_atualizados = [('Meireles', 1), ('Silva', 2), ('Santos', 3)]

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET sobrenome=%s WHERE id=%s'
        cursor.executemany(sql, dados_atualizados)
        conexao.commit()

#Selecionando o BD
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall() #há três fet

        for linhas in resultado:
            print(linhas)
