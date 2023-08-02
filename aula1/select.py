import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, wight = row
    print(_id, name, wight)

print('-' * 10)

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = 1')

row = cursor.fetchone()
_id, name, wight = row
print(_id, name, wight)

cursor.close()
connection.close()
