import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'custumers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# P E R I G O - Deleta a tabela

cursor.execute(f'DELETE FROM {TABLE_NAME}')
connection.commit()

# Deleta o id (sequencial)

cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weigth REAL'
    ')'
)


connection.commit()


# Inserir um valor na tabela

queryInsert = (f'INSERT INTO {TABLE_NAME} (name, weigth)'
               'VALUES'
               '(:nome, :peso)'
               )

# Executa uma vez só
# cursor.execute(queryInsert, ['Buga', 3])

# Insert de varios valores
cursor.executemany(queryInsert, [['Lucas', 1], ['Rau', 2], ['Sky', 3]])

# Insert com dicionarios
cursor.executemany(queryInsert, (
    {'nome': 'Lucas', 'peso': 1},
    {'nome': 'Rau', 'peso': 3},
    {'nome': 'Sky', 'peso': 4},

))


# DELETE
cursor.execute(f'DELETE FROM {TABLE_NAME} where id = 1')


# INSERT
cursor.execute(f'UPDATE {TABLE_NAME} SET name = "bubum" WHERE name = "Sky" ')


connection.commit()

cursor.close()
connection.close()
