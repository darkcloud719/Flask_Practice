import sqlite3

conn = sqlite3.connect('test2db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     age INTEGER           
    )
''')

cursor.execute("INSERT INTO user (name, age) VALUES (?,?)",("Alice",30))

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()