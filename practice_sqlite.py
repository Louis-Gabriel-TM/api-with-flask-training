import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table_query = '''CREATE TABLE Users (
    id INT,
    username TEXT,
    password TEXT
);'''
cursor.execute(create_table_query)

user = (1, "Bob", "pwd")
insert_query = 'INSERT INTO Users VALUES (?, ?, ?);'
cursor.execute(insert_query, user)

users = [
    (2, "Rolf", "azerty"),
    (3, "Anna", "123456")
]
cursor.executemany(insert_query, users)

select_query = 'SELECT * FROM Users;'
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
