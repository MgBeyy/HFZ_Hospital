from PyQt5.QtWidgets import QMainWindow

from UI import mainAsistant as ma
from Controller import loginController, addPatientController, asistantAppointmantController

class AsistantUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.asistantUi = ma.Ui_MainWindow()
        self.asistantUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.asistantUi.logOutButton.clicked.connect(self.logOut)
        self.asistantUi.prescriptionButton.clicked.connect(self.prescription)
        self.asistantUi.addPatient.clicked.connect(self.addPatient)

    def logOut(self):
        # Yapılan değişiklikleri sil
        self.login = loginController.loginUi()
        self.hide()
        self.login.show()

    def prescription(self):
        self.asAp = asistantAppointmantController.asistantAppointmantUi()
        self.asAp.show()

    def addPatient(self):
        self.addPatient = addPatientController.addPatientUi()
        self.addPatient.show()

