from PyQt5.QtWidgets import QMainWindow

from UI import login as l
from Controller import doctorController, asisstantController, patientController, forgotPassController

class loginUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.loginUi = l.Ui_MainWindow()
        self.loginUi.setupUi(self)
        self.setWindowTitle("HFZ Hastanesi")

        self.loginUi.loginButton.clicked.connect(self.login)
        self.loginUi.forgotPassButton.clicked.connect(self.forgotPass)

    def clear(self):
        self.loginUi.tcNoLineEdit.clear()
        self.loginUi.passwordLineEdit.clear()
        self.loginUi.labelInfo.setText("")

    def login(self):
        if self.loginUi.tcNoLineEdit.text() == 'd':
            self.clear()
            self.hide()
            self.doctorUi = doctorController.DoctorUi()
            self.doctorUi.show()

        elif self.loginUi.tcNoLineEdit.text() == 'p':
            self.clear()
            self.hide()
            self.patientUi = patientController.PatientUi()
            self.patientUi.show()

        elif self.loginUi.tcNoLineEdit.text() == 'a':
            self.clear()
            self.hide()
            self.asistantUi = asisstantController.AsistantUi()
            self.asistantUi.show()

        else:
            self.loginUi.labelInfo.setText("Hatalı Giriş!")
            print("Hatalı Giriş.")

    def forgotPass(self):
        self.clear()
        self.hide()
        self.forgotUi = forgotPassController.ForgotPassUi()
        self.forgotUi.show()