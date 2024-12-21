from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from UI import mainDoctor as md
from Controller import loginController, prescriptionController

class DoctorUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.doctorUi = md.Ui_MainWindow()
        self.doctorUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = None

        self.doctorUi.logOutButton.clicked.connect(self.logOut)
        self.doctorUi.prescriptionButton.clicked.connect(self.prescription)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")

    def logOut(self):
        # Yapılan değişiklikleri sil
        self.login = loginController.loginUi(self.database_connection)
        self.close()
        self.login.show()

    def prescription(self):
        self.pUi = prescriptionController.prescriptionUi()
        self.database_signal.connect(self.pUi.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.pUi.show()
