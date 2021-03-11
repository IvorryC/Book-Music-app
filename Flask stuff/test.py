import sqlite3

connection = sqlite3.connect('data.db')

curser = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
curser.execute(create_table)

user = (1, 'jose', 'momo')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
curser.execute(insert_query, user)

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'wxyz')
]
curser.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in curser.execute(select_query):
    print(row)

connection.commit()

connection.close()
