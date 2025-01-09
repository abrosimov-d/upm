import sqlite3
import sqlitecloud

class DB():
    def __init__(self, filename):
        self.connection = sqlitecloud.connect("sqlitecloud://ccfoathvhk.g1.sqlite.cloud:8860/snapshots?apikey=8aEet0uwk5bQhVuOihgCczIM928zRKoSbGMYQ8YdSoI")
        self.cursor = self.connection.cursor()

    def create(self, table, scheme):
        query = f'CREATE TABLE IF NOT EXISTS {table}({', '.join(f'{key} {scheme[key]}' for key in scheme)})'
        self.cursor.execute(query)
        self.connection.commit()

    def get_data(self, table):
        query = f'SELECT * from {table}'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def insert_data(self, table, data):
        query = f'INSERT INTO {table}({', '.join(key for key in data)}) VALUES({', '.join('?' for key in data)})'
        print(query)
        values = [str(data[key]) for key in data]
        self.cursor.execute(query, values)
        self.connection.commit()

    def update_data(self, data):
        pass

    def delete_data(self, table, id):
        query = f'DELETE FROM {table} WHERE id = ?'
        self.cursor.execute(query, (id,))

    def drop_table(self, table):
        query = f'DROP TABLE {table}'
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()
