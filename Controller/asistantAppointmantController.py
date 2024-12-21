from PyQt5.QtWidgets import QMainWindow

from UI import asistantAppointment


class asistantAppointmantUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.aaUi = asistantAppointment.Ui_MainWindow()
        self.aaUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = None

        self.aaUi.exitButton.clicked.connect(self.close)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")
