import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table_query = """CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);"""
cursor.execute(create_table_query)

create_table_query = """CREATE TABLE IF NOT EXISTS Items(
    name TEXT,
    price REAL
);"""
cursor.execute(create_table_query)

connection.commit()
connection.close()