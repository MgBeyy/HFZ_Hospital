from PyQt5.QtWidgets import QMainWindow

from UI import patientAppointment as pa

class patinetAppointmenUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.appUi = pa.Ui_MainWindow()
        self.appUi.setupUi(self)
        self.show()

        self.appUi.exitButton.clicked.connect(self.close)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")
