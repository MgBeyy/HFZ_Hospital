from PyQt5.QtWidgets import QMainWindow

from UI import addPatient


class addPatientUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.apUi = addPatient.Ui_MainWindow()
        self.apUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = None

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")
