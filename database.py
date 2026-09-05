import sqlite3

connection = sqlite3.connect("database.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    price REAL,
    servings INTEGER
)
""")

connection.commit()
connection.close()
