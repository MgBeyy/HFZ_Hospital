import pyodbc
import os



class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.server = "DESKTOP-97VLS18"
        self.database = "HFZ_Hospital"


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