from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import login as l
from UI import forgotPass as fp
from UI import mainDoctor as md
from UI import mainAsistant as ma
from UI import mainPatient as mp


def logOut(screen):
    screen.hide()
    window.show()



class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.loginUi = l.Ui_MainWindow()
        self.setWindowTitle("HFZ Hastanesi")
        self.loginUi.setupUi(self)

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
            self.doctorUi = DoctorUi()
            self.doctorUi.show()

        elif self.loginUi.tcNoLineEdit.text() == 'p':
            self.clear()
            self.hide()
            self.patientUi = PatientUi()
            self.patientUi.show()

        elif self.loginUi.tcNoLineEdit.text() == 'a':
            self.clear()
            self.hide()
            self.asistantUi = AsistantUi()
            self.asistantUi.show()

        else:
            self.loginUi.labelInfo.setText("Hatalı Giriş!")
            print("Hatalı Giriş.")

    def forgotPass(self):
        self.clear()
        self.hide()
        self.forgotUi = ForgotPassUi()
        self.forgotUi.show()


class ForgotPassUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.forgotUi = fp.Ui_MainWindow()
        self.forgotUi.setupUi(self)

        self.forgotUi.logInButton.clicked.connect(self.logIn)

    def clear(self):
        self.forgotUi.forgotPassTC.clear()
        self.forgotUi.forgotPassPhone.clear()
        self.forgotUi.forgotPassEPosta.clear()

    def logIn(self):
        self.clear()
        self.hide()
        self.logInUi = Main()
        self.logInUi.show()


class DoctorUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.doctorUi = md.Ui_MainWindow()
        self.setWindowTitle("HFZ Hastanesi")
        self.doctorUi.setupUi(self)

        self.doctorUi.logOutButton.clicked.connect(self.logOut)

    def logOut(self):
        logOut(self)


class AsistantUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.asistantUi = ma.Ui_MainWindow()
        self.setWindowTitle("HFZ Hastanesi")
        self.asistantUi.setupUi(self)

        self.asistantUi.logOutButton.clicked.connect(self.logOut)

    def logOut(self):
        logOut(self)


class PatientUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.patientUi = mp.Ui_MainWindow()
        self.setWindowTitle("HFZ Hastanesi")
        self.patientUi.setupUi(self)

        self.patientUi.logOutButton.clicked.connect(self.logOut)

    def logOut(self):
        logOut(self)


App = QApplication([])
window = Main()
window.show()
App.exec()