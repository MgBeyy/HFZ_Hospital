import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.server = os.getenv('DB_SERVER')
        self.database = os.getenv('DB_NAME')
        self.username = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')

    def connect(self):
        try:
            connection_string = f"""
                DRIVER={{SQL Server}};
                SERVER={self.server};
                DATABASE={self.database};
                Trusted_Connection=True;
            """
            self.conn = pyodbc.connect(connection_string)
            return self.conn
        except pyodbc.Error as e:
            print(f"Error connecting to database: {str(e)}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()