from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from UI import mainAsistant as ma
from Controller import loginController, addPatientController, asistantAppointmantController

class AsistantUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.asistantUi = ma.Ui_MainWindow()
        self.asistantUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = None

        self.asistantUi.logOutButton.clicked.connect(self.logOut)
        self.asistantUi.prescriptionButton.clicked.connect(self.prescription)
        self.asistantUi.addPatient.clicked.connect(self.addPatient)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")

    def logOut(self):
        # Yapılan değişiklikleri sil
        self.login = loginController.loginUi(self.database_connection)
        self.close()
        self.login.show()

    def prescription(self):
        self.asAp = asistantAppointmantController.asistantAppointmantUi()
        self.database_signal.connect(self.asAp.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.asAp.show()

    def addPatient(self):
        self.addPatient = addPatientController.addPatientUi()
        self.database_signal.connect(self.addPatient.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.addPatient.show()

