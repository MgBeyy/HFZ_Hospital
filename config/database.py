import pyodbc


class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.server = "localhost"  # Docker üzerinde MSSQL Server, localhost
        self.database = "HFZ_Hospital"  # Veritabanı adı
        self.username = "SA"  # SQL Server kullanıcı adı
        self.password = "StrongPassword123!"  # SQL Server parolası

    def connect(self):
        try:
            # MSSQL Server bağlantı stringi
            connection_string = f"""
                DRIVER={{ODBC Driver 17 for SQL Server}};
                SERVER={self.server};
                DATABASE={self.database};
                UID={self.username};
                PWD={self.password};
            """
            # Bağlantıyı kurma
            self.conn = pyodbc.connect(connection_string)
            print("Connection successful!")
            return self.conn
        except pyodbc.Error as e:
            print(f"Error connecting to database: {str(e)}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")







"""import pyodbc
import os



class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.server = "DESKTOP-97VLS18"
        self.database = "HFZ_Hospital"


    def connect(self):
        try:
            connection_string = f
                DRIVER={{SQL Server}};
                SERVER={self.server};
                DATABASE={self.database};
                Trusted_Connection=True;
            
            self.conn = pyodbc.connect(connection_string)
            return self.conn
        except pyodbc.Error as e:
            print(f"Error connecting to database: {str(e)}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()"""