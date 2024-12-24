from PyQt5.QtWidgets import QApplication

from Controller import loginController
from config import database

import os

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"D:\Ders Notları\Veritabanı Yönetim Sistemleri\Project\HFZ_Hospital\.venv\Lib\site-packages\PyQt5\Qt5\plugins"

try:
    database = database.DatabaseConnection()
    database_connection = database.connect()
except Exception as e:
    print(f"SQL Servera bağlanılamadı. Hata: {e}")
    exit()

App = QApplication([])
window = loginController.loginUi(database_connection)
window.show()
App.exec()
