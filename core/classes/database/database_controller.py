import sqlite3 as sql

class DatabaseController:
    def __init__(self, db_name: str):
        self.db_name = db_name
        
        self.connection = None
        self.cursor = None
    
    def connect(self):
        self.connection = sql.connect(self.db_name)
        self.cursor = self.connection.cursor()
        
    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        
    def execute(self, query_name: str, args: list=[], fetch_count: int=-1):
        pass