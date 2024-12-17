from PyQt5.QtWidgets import QMainWindow

from UI import mainPatient as mp
from Controller import loginController

class PatientUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.patientUi = mp.Ui_MainWindow()
        self.patientUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.patientUi.logOutButton.clicked.connect(self.logOut)

    def logOut(self):
        # Yapılan değişiklikleri sil
        self.login = loginController.loginUi()
        self.close()
        self.login.show()
