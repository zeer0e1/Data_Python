import os
import pymysql
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    passwd=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    port=(7777),
    cursorclass=pymysql.cursors.DictCursor
)

TABLE_NAME = 'CUSTOMERS'

# CURSOR DE CONECCÃO
with connection:
    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        # cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
    connection.commit()
        # consultando 

    # with connection.cursor() as cursor:
    #     id_recebido = input('Digite um id: ')
    #     coluna = 'id'
    #     sql = (f'SELECT * FROM {TABLE_NAME} WHERE {coluna} = %s')
    #     cursor.execute(sql, (id_recebido))
    #     print(cursor.mogrify(sql, (id_recebido)))
    #     data5 = cursor.fetchall()
    #     for row in data5:
    #         print(row)

        # Deletando
    # with connection.cursor() as cursor:
    #     id_recebido = input('Digite um id: ')
    #     coluna = 'id'
    #     sql = (f'DELETE FROM {TABLE_NAME} WHERE {coluna} = %s')
    #     query_consulta = f'SELECT * FROM {TABLE_NAME}'
    #     cursor.execute(sql, (id_recebido))
    #     data5 = cursor.fetchall()
    #     for row in data5:
    #         print(row)
    with connection.cursor() as cursor:
        query = (f'SELECT * FROM {TABLE_NAME}')
        cursor.execute(query)
        for row in cursor.fetchall():
            _id, name, age = row
            print(_id, name, age)
        
    connection.commit()
"""
    with connection.cursor() as cursor:
        # Comandos de insert
        sql = (
             f'INSERT INTO {TABLE_NAME} '
             '(nome, idade) '
             'VALUES (%(nome)s,%(idade)s) '
        )

        # insert 1
        data = {
            "nome": "Lucasf",
            "idade": 30
        }

        # insert 2
        data2 = {
            "idade": 25,
            "nome": "Le"
        }

        # insert 3
        data3 = (
            {"nome": "Ram", "idade": 50, },
            {"nome": "Terry", "idade": 13, },
            {"nome": "Pow", "idade": 25, }
        )
        result = cursor.executemany(sql, data3)
        print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
             f'INSERT INTO {TABLE_NAME} '
             '(nome, idade) '
             'VALUES (%s,%s) '
        )

        data4 = (
             ("Siri", 1),
             ("Cortana", 2),
        )
        cursor.executemany(sql, data4)
    connection.commit()
"""
