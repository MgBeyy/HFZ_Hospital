from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from UI import mainPatient as mp
from Controller import loginController, patientAppointmentController
from config import database


class PatientUi(QMainWindow):
    database_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.patientUi = mp.Ui_MainWindow()
        self.patientUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.database_connection = None

        self.patientUi.logOutButton.clicked.connect(self.logOut)
        self.patientUi.getAppointmentButton.clicked.connect(self.getAppointment)

    def set_database_connection(self, database_connection):
        self.database_connection = database_connection
        print("Database bağlantısı alındı")

    def logOut(self):
        # Yapılan değişiklikleri sil
        self.login = loginController.loginUi(self.database_connection)
        self.close()
        self.login.show()

    def getAppointment(self):
        self.appUi = patientAppointmentController.patinetAppointmenUi()
        self.database_signal.connect(self.appUi.set_database_connection)
        self.database_signal.emit(self.database_connection)
        self.appUi.show()
