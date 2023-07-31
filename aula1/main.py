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
cursor.execute(f'INSERT INTO {TABLE_NAME} (id, name, weigth)'
               'VALUES (NULL, "Skysauro", 2), (NULL, "Rauana Ribeiro", 14.5)'
               )
# varios valores  cursor.executemany()

connection.commit()


cursor.close()
connection.close()
