from PyQt5.QtWidgets import QMainWindow

from UI import mainDoctor as md
from Controller import loginController

class DoctorUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.doctorUi = md.Ui_MainWindow()
        self.doctorUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.doctorUi.logOutButton.clicked.connect(self.logOut)

    def logOut(self):
        # Yapılan değişiklikleri sil
        self.login = loginController.loginUi()
        self.hide()
        self.login.show()
