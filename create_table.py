import sqlite3

connection = sqlite3.connect("todo.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS db (id INTEGER PRIMARY KEY, name text, is_executed INTEGER DEFAULT 0 CHECK(is_executed IN (0,1)))"
cursor.execute(create_table)

connection.commit()
connection.close()