import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("../database.sqlite3")
        self.cursor = self.conn.cursor()

        # create table for channels
        self.cursor.execute("""create table if not exists channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel text
        )""")
        
        # create table for phrases
        self.cursor.execute("""create table if not exists phrases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phrase text
        )""")

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def __del__(self):
        self.conn.close()


db = Database()
print(db.fetchall("select * from channels"))
